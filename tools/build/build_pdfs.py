"""Builds the readable PDFs from the Markdown source.
Run from the repository root:  python tools/build/build_pdfs.py
Needs: pandoc 3.x, Python 'playwright' with Chrome/Chromium."""
import os, subprocess, base64, asyncio, glob, sys
ROOT=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
B=os.path.join(ROOT,'tools','build'); DIST=os.path.join(ROOT,'dist'); os.makedirs(DIST,exist_ok=True)
CH=sorted(glob.glob(os.path.join(ROOT,'content','*.md')))
VERSION='3.0 (Stage 3 final) · 25 November 2026'
logo=base64.b64encode(open(os.path.join(ROOT,'assets','brand','csmaxxxing-logo-small.png'),'rb').read()).decode()

def cover(title,sub,extra):
    return f'''<div class="cover"><img class="logo" src="../assets/brand/csmaxxxing-logo.png" alt="CSMAXXXING logo">
<h1>{title}</h1><div class="sub">{sub}</div><img class="max" src="../assets/brand/max-mascot.png" alt="Max the Agent">
<table><tr><td><b>Team</b></td><td>CSMAXXXING</td></tr><tr><td><b>Module</b></td><td>AI Overview, Chapters 1–8</td></tr>
<tr><td><b>Version</b></td><td>{VERSION}</td></tr>{extra}</table></div>'''

def pandoc(out_html, before, move, title):
    open(os.path.join(DIST,'_before.html'),'w').write(before)
    env=dict(os.environ, MOVE_ANSWERS='1' if move else '0')
    cmd=['pandoc',*CH,'-f','markdown+fenced_divs+bracketed_spans','-t','html5','-s','--section-divs','--toc','--toc-depth=2',
         '--lua-filter',os.path.join(B,'boxes.lua'),'--css','../tools/build/style.css','--include-before-body',os.path.join(DIST,'_before.html'),
         '--metadata','title='+title,'--metadata','lang=en','-o',os.path.join(DIST,out_html)]
    subprocess.run(cmd,check=True,env=env,cwd=os.path.join(ROOT,'content'))
    import re
    h=open(os.path.join(DIST,out_html)).read()
    # keep the contents page short: drop routine sub-entries (they are still in every chapter)
    h=re.sub(r'<li><a href="#(ch\d-(sources|resources|takeaways)|qc\d)"[^>]*>.*?</a></li>\s*','',h,flags=re.S)
    open(os.path.join(DIST,out_html),'w').write(h)

async def pdf(html,out,label):
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        exe=os.environ.get('CHROME','/usr/bin/google-chrome')
        b=await p.chromium.launch(executable_path=exe if os.path.exists(exe) else None,args=['--no-sandbox'])
        pg=await b.new_page(); await pg.goto('file://'+os.path.join(DIST,html)); await pg.wait_for_timeout(800)
        head=f'<div style="width:100%;font-size:7.5pt;font-family:Arial;color:#6B6B75;padding:0 17mm;display:flex;align-items:center;gap:6px"><img src="data:image/png;base64,{logo}" style="height:9mm"><span>CSMAXXXING · {label}</span><span style="margin-left:auto">v3.0</span></div>'
        foot='<div style="width:100%;font-size:8pt;font-family:Arial;color:#6B6B75;text-align:center"><span class="pageNumber"></span> / <span class="totalPages"></span></div>'
        await pg.pdf(path=os.path.join(DIST,out),format='A4',print_background=True,display_header_footer=True,header_template=head,footer_template=foot,
                     margin={'top':'20mm','bottom':'16mm','left':'0','right':'0'},prefer_css_page_size=False)
        await b.close()

if __name__=='__main__':
    pandoc('markdown_content.html',cover('Readable Markdown Content','AI Overview: final Markdown source, rendered','<tr><td><b>Source</b></td><td>content/*.md in the repository</td></tr>'),False,'CSMAXXXING Markdown Content v3.0')
    pandoc('study_guide.html',cover('AI Overview Study Guide','Learn it. Try it. Teach Max.','<tr><td><b>Start at</b></td><td>“Start Here” (page 3), then Chapter 1</td></tr><tr><td><b>Activities</b></td><td>CSMAXXXING AI Lab (activities/ai-lab/index.html)</td></tr>'),True,'CSMAXXXING Study Guide v3.0')
    asyncio.run(pdf('markdown_content.html','CSMAXXXING_Readable_Markdown_Content_v3.0.pdf','Readable Markdown Content'))
    asyncio.run(pdf('study_guide.html','CSMAXXXING_Study_Guide_v3.0.pdf','AI Overview Study Guide'))
    for f in ['_before.html','markdown_content.html','study_guide.html']: os.remove(os.path.join(DIST,f))
    print('done')
