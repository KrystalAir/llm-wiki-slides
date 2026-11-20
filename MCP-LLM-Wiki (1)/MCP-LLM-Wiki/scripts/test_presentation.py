from pathlib import Path
from playwright.sync_api import sync_playwright
import json, re
root=Path(__file__).resolve().parents[1]
results=[]
(root/'workflow'/'evidence').mkdir(exist_ok=True)
with sync_playwright() as p:
    browser=p.chromium.launch(headless=True,**({'executable_path':'/usr/bin/chromium'} if Path('/usr/bin/chromium').exists() else {}),args=['--no-sandbox','--disable-gpu'])
    for width,height,label in [(1440,900,'desktop'),(390,844,'mobile')]:
        page=browser.new_page(viewport={'width':width,'height':height},device_scale_factor=1)
        errors=[]
        page.on('pageerror', lambda e: errors.append(str(e)))
        page.set_content((root/'presentation'/'index.html').read_text(encoding='utf-8'),wait_until='load')
        assert page.locator('.slide').count()==12
        assert page.locator('.slide.active').count()==1
        assert page.locator('#counter').inner_text()=='1 / 12'
        assert page.locator('#prev').is_disabled()
        assert page.locator('#next').is_enabled()
        slide_info=[]
        for i in range(12):
            if i>0:
                page.click('#next')
            assert page.locator('#counter').inner_text()==f'{i+1} / 12'
            assert page.locator('.slide.active').count()==1
            active=page.locator('.slide.active')
            assert len(active.get_attribute('data-sources'))>0
            assert active.locator('.slide-source a[target="_blank"]').count()>0
            # only visible active slide elements are considered for layout overflow
            metrics=page.evaluate('''() => {
                const vw=document.documentElement.clientWidth;
                const visible=[...document.querySelectorAll('.slide.active *')].filter(e=>{const r=e.getBoundingClientRect();return r.width>0&&r.height>0&&getComputedStyle(e).display!=='none'});
                const out=visible.filter(e=>{const r=e.getBoundingClientRect();return r.left< -1 || r.right>vw+1}).slice(0,8).map(e=>({tag:e.tagName,cl:e.className,text:(e.textContent||'').trim().slice(0,30),bounds:[Math.round(e.getBoundingClientRect().left),Math.round(e.getBoundingClientRect().right)]}));
                return {pageWidth:document.documentElement.scrollWidth,viewport:vw,outerOverflow:out,bodyScrollHeight:document.body.scrollHeight,viewHeight:innerHeight};}''')
            slide_info.append({'slide':i+1,'title':active.locator('h1').inner_text(),'metrics':metrics})
            if i==7:
                assert page.locator('#step-number').inner_text()=='1'
                for k in range(6):page.click('#step-next')
                assert page.locator('#step-number').inner_text()=='7'
                assert page.locator('#step-next').is_disabled()
                page.click('#step-prev')
                assert page.locator('#step-number').inner_text()=='6'
            if i==11:
                page.click('[data-quiz="0"][data-choice="0"]')
                assert '正確' in page.locator('#quiz-feedback-0').inner_text()
                page.click('[data-quiz="1"][data-choice="0"]')
                assert '再想想' in page.locator('#quiz-feedback-1').inner_text()
                assert page.locator('#next').is_disabled()
            if i in (0,3,5,7,11):
                page.wait_for_timeout(360)
                page.screenshot(path=str(root/'workflow'/'evidence'/f'test-{label}-{i+1:02}.png'),full_page=True)
        page.keyboard.press('ArrowLeft')
        assert page.locator('#counter').inner_text()=='11 / 12'
        page.keyboard.press('ArrowRight')
        assert page.locator('#counter').inner_text()=='12 / 12'
        # verify embedded Wiki source mapping points to a real local note
        for name in page.locator('.slide').evaluate_all('(slides)=>slides.map(s=>s.getAttribute("data-wiki"))'):
            assert (root/'wiki'/f'{name}.md').is_file(), name
        results.append({'device':label,'viewport':f'{width}x{height}','errors':errors,'slides':slide_info,
                        'horizontal_overflow_pages':[e for e in slide_info if e['metrics']['pageWidth']>e['metrics']['viewport']+1 or e['metrics']['outerOverflow']]})
        page.close()
    browser.close()
(out:=root/'workflow'/'browser-test-result.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
for r in results:
    print(r['device'],r['viewport'],'page_errors',r['errors'],'overflow',len(r['horizontal_overflow_pages']))
    for e in r['horizontal_overflow_pages']:
        print('  Slide',e['slide'], e['metrics'])
