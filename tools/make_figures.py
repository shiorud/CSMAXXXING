"""Regenerates every figure in assets/figures. Run: python tools/make_figures.py
Needs: numpy, matplotlib, pillow, scikit-image."""
import sys, random, numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch, Rectangle
from PIL import Image
import os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT=os.path.join(ROOT,'assets','figures')+'/'
sys.path.insert(0,os.path.join(ROOT,'activities','code'))
RED='#E8412F'; INK='#1F1F23'; BLUE='#2F6FDE'; AMBER='#F2A93B'; GREEN='#2BA36B'; GREY='#8A8A93'; SOFT='#FFF4F0'; PALE='#F4F5F7'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,'axes.edgecolor':INK,'axes.labelcolor':INK,'xtick.color':INK,'ytick.color':INK,'axes.spines.top':False,'axes.spines.right':False})
def save(fig,name): fig.savefig(OUT+name,dpi=150,bbox_inches='tight',facecolor='white'); plt.close(fig); print('saved',name)
def box(ax,x,y,w,h,text,fc=PALE,ec=INK,fs=13,tc=INK,bold=False,r=0.08):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0.02,rounding_size={r}',fc=fc,ec=ec,lw=1.6))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=fs,color=tc,weight='bold' if bold else 'normal',wrap=True)
def arrow(ax,a,b,c=INK,rad=0,lw=1.8,style='-|>'):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle=style,mutation_scale=18,color=c,lw=lw,connectionstyle=f'arc3,rad={rad}'))
def blank(w,h): 
    fig,ax=plt.subplots(figsize=(w,h)); ax.set_xlim(0,w); ax.set_ylim(0,h); ax.axis('off'); return fig,ax

# 1 timeline
fig,ax=blank(14,4.2)
ev=[(1950,'Turing asks\n"Can machines think?"'),(1956,'Dartmouth workshop\nnames "AI"'),(1966,'ELIZA chatbot'),(1974,'First "AI winter"'),
    (1980,'Expert systems boom'),(1997,'Deep Blue beats\nKasparov at chess'),(2012,'Deep learning wins\nImageNet (AlexNet)'),(2016,'AlphaGo beats\nLee Sedol at Go'),(2022,'ChatGPT released'),(2025,'DreamerV3 finds\nMinecraft diamonds')]
x0,x1=0.7,13.3
ax.plot([x0,x1],[2.1,2.1],color=INK,lw=3)
for i,(yr,t) in enumerate(ev):
    x=x0+(x1-x0)*i/(len(ev)-1); up=i%2==0; key=yr in (1956,2012,2022)
    ax.add_patch(Circle((x,2.1),0.14,color=RED if key else INK,zorder=3))
    ax.plot([x,x],[2.1,2.75 if up else 1.45],color=GREY,lw=1)
    ax.text(x,2.8 if up else 1.4,str(yr),ha='center',va='bottom' if up else 'top',fontsize=13,weight='bold',color=RED)
    ax.text(x,3.2 if up else 1.0,t,ha='center',va='bottom' if up else 'top',fontsize=10.5,color=INK)
save(fig,'ch1_timeline.png')

# 2 AI > ML > DL nested
fig,ax=blank(8,5.6)
for (w,h,c,t,yc) in [(7.6,5.2,'#FDE3DE','Artificial Intelligence\nmachines doing tasks that need "intelligence"',4.75),(5.8,3.6,'#FBC4BA','Machine Learning: learns patterns from data',3.75),(3.6,1.6,RED,'Deep Learning\nmany-layer neural networks',1.95)]:
    y0=0.2 if w>7 else (0.5 if w>5 else 1.15)
    ax.add_patch(FancyBboxPatch((4-w/2,y0),w,h,boxstyle='round,pad=0.02,rounding_size=0.4',fc=c,ec=INK,lw=1.5))
    ax.text(4,yc,t,ha='center',va='center',fontsize=12,color='white' if c==RED else INK,weight='bold')
save(fig,'ch1_ai_ml_dl.png')

# 3 five-step cycle
fig,ax=blank(14,4.2)
steps=[('1 INPUT','collect & sort data'),('2 PROCESSING','find patterns'),('3 OUTCOMES','predict: pass or fail?'),('4 ADJUSTMENTS','learn from the fails'),('5 ASSESSMENTS','check results, feed back')]
for i,(a,b) in enumerate(steps):
    x=0.2+i*2.8; box(ax,x,1.5,2.3,1.2,'',fc='#FDE3DE' if i==3 else SOFT,ec=RED if i==3 else INK)
    ax.text(x+1.15,2.3,a,ha='center',fontsize=13,weight='bold',color=RED if i==3 else INK); ax.text(x+1.15,1.85,b,ha='center',fontsize=10.5)
    if i<4: arrow(ax,(x+2.32,2.1),(x+2.78,2.1))
arrow(ax,(0.2+3*2.8+0.6,1.48),(0.2+2*2.8+1.7,1.48),c=RED,rad=-0.6,lw=2.2)
ax.text(0.2+2.5*2.8+1.15,0.45,'"fail"? adjust the rules and try the outcomes again',ha='center',fontsize=11,color=RED,style='italic')
arrow(ax,(0.2+4*2.8+1.15,2.72),(0.2+1.15,2.72),c=BLUE,rad=0.18,lw=2)
ax.text(7,4.0,'feedback loop: assessments feed into the next round of input',ha='center',fontsize=11,color=BLUE,style='italic')
save(fig,'ch2_five_steps.png')

# 4 cat as numbers
cat=np.array(Image.open(os.path.join(ROOT,'assets','photos','chelsea.png')).convert('L'))
fig,axs=plt.subplots(1,3,figsize=(14,4.6),gridspec_kw={'width_ratios':[1.5,1,1.1]})
axs[0].imshow(Image.open(os.path.join(ROOT,'assets','photos','chelsea.png'))); axs[0].set_title('What you see',fontsize=14,weight='bold'); axs[0].axis('off')
y0,x0=95,150; axs[0].add_patch(Rectangle((x0,y0),60,60,fill=False,ec=RED,lw=3))
crop=cat[y0:y0+60,x0:x0+60]
axs[1].imshow(crop,cmap='gray',interpolation='nearest'); axs[1].set_title('Zoom: tiny squares (pixels)',fontsize=14,weight='bold'); axs[1].axis('off')
small=crop[20:28,20:28]
axs[2].imshow(small,cmap='gray',vmin=0,vmax=255); axs[2].axis('off'); axs[2].set_title('What the computer sees',fontsize=14,weight='bold')
for i in range(8):
    for j in range(8):
        v=small[i,j]; axs[2].text(j,i,str(v),ha='center',va='center',fontsize=9.5,color='white' if v<128 else 'black')
save(fig,'ch2_cat_as_numbers.png')

# 5 structured vs unstructured
fig,ax=blank(12,4.6)
ax.text(3,4.3,'STRUCTURED data',ha='center',fontsize=15,weight='bold',color=BLUE)
rows=[['Name','Age','City'],['Ana','19','Beijing'],['Ben','21','Shanghai'],['Chen','20','Wuhan']]
for i,r in enumerate(rows):
    for j,v in enumerate(r):
        ax.add_patch(Rectangle((0.6+j*1.6,3.3-i*0.7),1.6,0.7,fc='#DCE8FB' if i==0 else 'white',ec=INK))
        ax.text(1.4+j*1.6,3.65-i*0.7,v,ha='center',va='center',fontsize=12,weight='bold' if i==0 else 'normal')
ax.text(3,0.3,'rows & columns: easy for rules to read',ha='center',fontsize=11.5,style='italic')
ax.text(9,4.3,'UNSTRUCTURED data',ha='center',fontsize=15,weight='bold',color=RED)
ax.imshow(Image.open(os.path.join(ROOT,'assets','photos','coffee.png')),extent=(6.6,8.6,2.3,3.6))
ax.text(9.9,3.05,'"Can you bring\nme a coffee? :)"',ha='center',va='center',fontsize=12,bbox=dict(boxstyle='round',fc='#FDE3DE',ec=RED))
t=np.linspace(0,1,300); ax.plot(6.7+2*t,1.5+0.35*np.sin(40*t)*np.exp(-2*t),color=INK)
ax.text(7.7,1.0,'audio',ha='center',fontsize=11); ax.text(7.6,2.05,'photo',ha='center',fontsize=11); ax.text(9.9,2.05,'text',ha='center',fontsize=11)
ax.add_patch(Rectangle((9.1,1.15),1.6,0.7,fc=INK)); ax.text(9.9,1.5,'▶ video',color='white',ha='center',va='center',fontsize=12)
ax.text(9,0.3,'no fixed table: most of the world\'s data',ha='center',fontsize=11.5,style='italic')
save(fig,'ch2_structured_unstructured.png')

# 6 three ways machines learn
fig,axs=plt.subplots(1,3,figsize=(14,4.5))
rng=np.random.default_rng(3)
a=rng.normal([1,1],0.45,(30,2)); b=rng.normal([3,3],0.45,(30,2))
axs[0].scatter(*a.T,c=BLUE,s=45,marker='o',label='cat'); axs[0].scatter(*b.T,c=RED,s=55,marker='^',label='dog'); axs[0].plot([0,4],[4,0],'--',color=INK)
axs[0].legend(loc='upper left',fontsize=11); axs[0].set_title('Supervised\nlearn from LABELLED examples',fontsize=13,weight='bold')
c=np.vstack([a,b,rng.normal([1,3.2],0.4,(30,2))])
axs[1].scatter(*c.T,c=GREY,s=45); 
for ctr in [(1,1),(3,3),(1,3.2)]: axs[1].add_patch(Circle(ctr,0.95,fill=False,ec=AMBER,lw=2.5,ls='--'))
axs[1].set_title('Unsupervised\nfind GROUPS with no labels',fontsize=13,weight='bold')
ax=axs[2]; ax.set_xlim(0,4); ax.set_ylim(0,4)
box(ax,0.2,2.6,1.4,0.9,'Agent',fc='#FDE3DE',ec=RED,bold=True); box(ax,2.4,0.5,1.4,0.9,'World',fc='#DCE8FB',ec=BLUE,bold=True)
arrow(ax,(1.6,3.05),(3.1,1.45),rad=-0.3); arrow(ax,(2.4,0.95),(0.9,2.6),rad=-0.3)
ax.text(2.9,2.8,'action',fontsize=12); ax.text(0.15,1.1,'reward +\nnew state',fontsize=12)
ax.set_title('Reinforcement\nlearn from REWARDS by trial & error',fontsize=13,weight='bold')
for a_ in axs: a_.set_xticks([]); a_.set_yticks([])
save(fig,'ch2_three_ways_to_learn.png')

# 7 overfitting
rng=np.random.default_rng(7); x=np.sort(rng.uniform(0,6,14)); y=0.6*x+1+rng.normal(0,0.5,14)
fig,axs=plt.subplots(1,2,figsize=(12,4.3))
xs=np.linspace(0,6,300)
for ax,deg,t,c in [(axs[0],1,'Good fit: learns the TREND',GREEN),(axs[1],11,'Overfit: MEMORISES the noise',RED)]:
    p=np.polyfit(x,y,deg); ax.plot(xs,np.clip(np.polyval(p,xs),-1,7),color=c,lw=2.5); ax.scatter(x,y,color=INK,zorder=3,s=40)
    ax.set_ylim(-1,7); ax.set_title(t,fontsize=14,weight='bold',color=c); ax.set_xlabel('study hours'); ax.set_ylabel('test score')
save(fig,'ch2_overfitting.png')

# 8 capability ladder
fig,ax=blank(10,5.2)
lv=[('Narrow AI (Weak AI)','one task, often better than humans','EXISTS TODAY: Siri, ChatGPT, spam filters',GREEN),('General AI (AGI / Strong AI)','any intellectual task a human can do','THEORETICAL',AMBER),('Super AI','surpasses humans at everything','THEORETICAL',RED)]
for i,(a,b,c,col) in enumerate(lv):
    x=0.3+i*1.2; y=0.3+i*1.55
    box(ax,x,y,6.6,1.3,'',fc='white',ec=col)
    ax.add_patch(Rectangle((x,y),0.25,1.3,color=col))
    ax.text(x+0.5,y+0.98,a,fontsize=14,weight='bold',va='center'); ax.text(x+0.5,y+0.6,b,fontsize=12,va='center')
    ax.text(x+0.5,y+0.24,c,fontsize=10.5,va='center',color=col,weight='bold')
arrow(ax,(9.4,0.4),(9.4,4.9),c=GREY,lw=3); ax.text(9.6,2.6,'capability',rotation=90,va='center',color=GREY,fontsize=12)
save(fig,'ch3_capability_ladder.png')

# 9 functional types grid
fig,ax=blank(11,4.6)
ft=[('Reactive machines','no memory;\nreacts only to\nwhat it sees now','e.g. Deep Blue\n(chess)',GREEN,'exists'),('Limited memory','uses recent data\nand past training','e.g. self-driving\ncars, chatbots',GREEN,'exists'),('Theory of mind','would understand\nothers\' thoughts\nand feelings','—',AMBER,'theoretical'),('Self-aware','would understand\nits own inner\nstates','—',RED,'theoretical')]
for i,(a,b,c,col,s) in enumerate(ft):
    x=0.2+i*2.7; box(ax,x,0.4,2.5,3.6,'',fc='white',ec=col)
    ax.add_patch(Rectangle((x,3.35),2.5,0.65,color=col)); ax.text(x+1.25,3.67,a,ha='center',va='center',color='white',fontsize=12.5,weight='bold')
    ax.text(x+1.25,2.5,b,ha='center',va='center',fontsize=11,wrap=True)
    ax.text(x+1.25,1.45,c,ha='center',va='center',fontsize=10.5,style='italic')
    ax.text(x+1.25,0.75,s.upper(),ha='center',va='center',fontsize=11,weight='bold',color=col)
save(fig,'ch3_functional_types.png')

# 10 real CV: face detection + edges
from skimage import data, feature, color, filters
img=data.astronaut(); det=feature.Cascade(data.lbp_frontal_face_cascade_filename())
faces=det.detect_multi_scale(img=img,scale_factor=1.2,step_ratio=1,min_size=(60,60),max_size=(300,300))
fig,axs=plt.subplots(1,2,figsize=(12,6))
axs[0].imshow(img); 
for f in faces: axs[0].add_patch(Rectangle((f['c'],f['r']),f['width'],f['height'],fill=False,ec=RED,lw=3)); axs[0].text(f['c'],f['r']-8,'face',color='white',fontsize=13,weight='bold',bbox=dict(fc=RED,ec='none'))
axs[0].set_title('Object detection: a real face detector\nfound and boxed the face',fontsize=13,weight='bold'); axs[0].axis('off')
axs[1].imshow(filters.sobel(color.rgb2gray(data.chelsea())),cmap='gray_r'); axs[1].axis('off')
axs[1].set_title('Edge detection: the outlines a vision\nsystem starts from',fontsize=13,weight='bold')
print('faces',len(faces)); save(fig,'ch4_computer_vision_demo.png')

# 11 traditional vs ML
fig,ax=blank(12,4.4)
for row,(lab,ins,out,col) in enumerate([('Traditional programming',('Rules','Data'),'Answers',BLUE),('Machine learning',('Data','Answers'),'Rules (a model)',RED)]):
    y=2.6-row*2.1
    ax.text(0.1,y+0.95,lab,fontsize=14,weight='bold',color=col)
    box(ax,0.3,y+0.15,1.6,0.6,ins[0]); box(ax,0.3,y-0.6,1.6,0.6,ins[1])
    box(ax,4.3,y-0.35,2.6,0.9,'Computer',fc=col,tc='white',bold=True,ec=col)
    box(ax,9.0,y-0.3,2.7,0.8,out,fc='#FDE3DE' if col==RED else '#DCE8FB',ec=col,bold=True)
    arrow(ax,(1.95,y+0.45),(4.25,y+0.15)); arrow(ax,(1.95,y-0.3),(4.25,y)); arrow(ax,(6.95,y+0.1),(8.95,y+0.1))
save(fig,'ch5_traditional_vs_ml.png')

# 12 knowledge base & inference
fig,ax=blank(12,4.4)
box(ax,0.2,0.4,3.6,3.5,'',fc='#DCE8FB',ec=BLUE); ax.text(2,3.55,'KNOWLEDGE BASE',ha='center',weight='bold',color=BLUE)
ax.text(0.4,2.6,'Facts:\n  has(pat, fever)\n  has(pat, cough)\n  has(pat, short_breath)',fontsize=11,family='DejaVu Sans Mono',va='center')
ax.text(0.4,1.1,'Rule:\n  IF fever AND cough\n  AND short_breath\n  THEN may_have_pneumonia',fontsize=10.5,family='DejaVu Sans Mono',va='center')
box(ax,4.7,1.4,2.8,1.4,'INFERENCE\nENGINE\nmatches facts\nto rules',fc=INK,tc='white',ec=INK,bold=True)
box(ax,8.4,1.55,3.4,1.1,'Conclusion:\npat may have pneumonia',fc='#FDE3DE',ec=RED,bold=True)
arrow(ax,(3.85,2.1),(4.65,2.1)); arrow(ax,(7.55,2.1),(8.35,2.1))
ax.text(10.1,0.9,'+ explanation: "because rule 1\nmatched fever, cough, short_breath"',ha='center',fontsize=10.5,style='italic',color=RED)
save(fig,'ch6_knowledge_base.png')

# 13 family tree
fig,ax=blank(8,5)
nodes={'tom':(4,4.3),'alice':(4,3.0),'bob':(2.6,1.7),'carol':(5.4,1.7),'dave':(2.6,0.4)}
for a,b in [('tom','alice'),('alice','bob'),('alice','carol'),('bob','dave')]:
    arrow(ax,(nodes[a][0],nodes[a][1]-0.3),(nodes[b][0],nodes[b][1]+0.3))
for n,(x,y) in nodes.items(): box(ax,x-0.7,y-0.28,1.4,0.56,n,fc='white',ec=INK,bold=True)
ax.text(6.0,4.3,'arrow = parent(X, Y)',fontsize=11,style='italic',color=GREY)
save(fig,'ch6_family_tree.png')

# 14 canteen neuron
fig,ax=blank(11,4.8)
ins=[('Friend going?','+2',BLUE),('Raining?','−3',RED),('Hungry?','+2',BLUE)]
for i,(t,w,c) in enumerate(ins):
    y=3.9-i*1.4; box(ax,0.2,y-0.35,2.4,0.7,t,fc='white'); arrow(ax,(2.65,y),(5.0,2.5),c=c,lw=1.5+abs(int(w.replace('−','-')))*0.7)
    ax.text(3.6,(y+2.5)/2+0.18,'w = '+w,fontsize=13,weight='bold',color=c)
ax.add_patch(Circle((5.8,2.5),0.85,fc=INK)); ax.text(5.8,2.65,'Σ',color='white',fontsize=26,ha='center',va='center'); ax.text(5.8,2.1,'add up',color='white',fontsize=10,ha='center')
box(ax,7.2,2.0,1.9,1.0,'total ≥ 2 ?',fc='#FDE3DE',ec=RED,bold=True); arrow(ax,(6.65,2.5),(7.15,2.5))
box(ax,9.6,2.85,1.2,0.7,'GO',fc=GREEN,tc='white',bold=True,ec=GREEN); box(ax,9.6,1.45,1.2,0.7,'stay',fc=GREY,tc='white',bold=True,ec=GREY)
arrow(ax,(9.1,2.7),(9.55,3.15)); arrow(ax,(9.1,2.3),(9.55,1.8)); ax.text(9.15,3.3,'yes',fontsize=10); ax.text(9.15,1.4,'no',fontsize=10)
save(fig,'ch7_canteen_neuron.png')

# 15 layers
fig,ax=blank(10,5)
L=[3,4,4,2]; xs=[1,3.6,6.2,8.8]; labels=['Input units','Hidden units','Hidden units','Output units']; P=[]
for k,(n,x) in enumerate(zip(L,xs)):
    ys=np.linspace(4,1,n) if n>1 else [2.5]; P.append([(x,y) for y in ys])
    ax.text(x,4.65,labels[k],ha='center',fontsize=12,weight='bold',color=[BLUE,INK,INK,RED][k])
rng=np.random.default_rng(2)
for a_,b_ in zip(P[:-1],P[1:]):
    for p in a_:
        for q in b_:
            w=rng.normal(); ax.plot([p[0],q[0]],[p[1],q[1]],color=BLUE if w>0 else RED,lw=0.5+1.6*abs(w),alpha=0.6)
for k,col in enumerate(P):
    for (x,y) in col: ax.add_patch(Circle((x,y),0.28,fc=[BLUE,'white','white',RED][k],ec=INK,lw=1.5,zorder=3))
ax.text(5,0.3,'line thickness = weight size   blue = positive   red = negative',ha='center',fontsize=11,style='italic')
save(fig,'ch7_network_layers.png')

# 16 gradient descent
fig,ax=plt.subplots(figsize=(8,4.4)); w=np.linspace(-3,5,300); loss=(w-2)**2/2+0.5
ax.plot(w,loss,color=INK,lw=2.5); pts=[-2.5]; 
for _ in range(6): pts.append(pts[-1]-0.45*(pts[-1]-2))
for i,p in enumerate(pts):
    ax.scatter(p,(p-2)**2/2+0.5,color=RED,s=80,zorder=3)
    if i: ax.annotate('',xy=(p,(p-2)**2/2+0.5),xytext=(pts[i-1],(pts[i-1]-2)**2/2+0.5),arrowprops=dict(arrowstyle='->',color=RED,lw=1.8))
ax.set_xlabel('value of one weight'); ax.set_ylabel('loss (how wrong)'); ax.set_title('Learning = walking downhill on the error',fontsize=14,weight='bold')
ax.annotate('best weight',xy=(2,0.5),xytext=(3.4,3.5),color=GREEN,weight='bold',arrowprops=dict(arrowstyle='->',color=GREEN)); ax.set_ylim(0,12)
save(fig,'ch7_gradient_descent.png')

# 17 network types
fig,axs=plt.subplots(1,4,figsize=(15,3.8))
titles=['Feedforward','Convolutional (CNN)','Recurrent (RNN)','Transformer']
subs=['one direction:\ninput → output','slides small filters\nover an image','loops back: remembers\nearlier items in a sequence','attention: every word\nlooks at every other word']
for ax,t,s in zip(axs,titles,subs):
    ax.set_xlim(0,4); ax.set_ylim(0,4); ax.axis('off'); ax.set_title(t,fontsize=14,weight='bold',color=RED); ax.text(2,0.15,s,ha='center',fontsize=11)
for i,y in enumerate([3,2.2]): pass
ax=axs[0]
for x in [0.7,2,3.3]:
    for y in [3.2,2.4,1.6]: ax.add_patch(Circle((x,y),0.2,fc='white',ec=INK))
for y in [3.2,2.4,1.6]:
    for y2 in [3.2,2.4,1.6]: ax.plot([0.9,1.8],[y,y2],color=GREY,lw=0.8); ax.plot([2.2,3.1],[y,y2],color=GREY,lw=0.8)
ax=axs[1]; g=np.array(Image.open(os.path.join(ROOT,'assets','photos','chelsea.png')).convert('L').resize((40,27)))
ax.imshow(g,cmap='gray',extent=(0.2,3.8,1.2,3.6)); ax.add_patch(Rectangle((1.4,2.0),0.6,0.6,fill=False,ec=RED,lw=3))
ax=axs[2]
for i,x in enumerate([0.6,1.6,2.6,3.6]):
    ax.add_patch(Circle((x,2.4),0.28,fc='white',ec=INK)); ax.text(x,1.6,['I','love','AI','!'][i],ha='center',fontsize=12)
    if i<3: arrow(ax,(x+0.3,2.4),(x+0.7,2.4),c=RED)
ax=axs[3]; words=['the','cat','sat','down']
for i,wd in enumerate(words): ax.text(0.6+i*0.95,3.2,wd,ha='center',fontsize=12,bbox=dict(fc='white',ec=INK)); ax.text(0.6+i*0.95,1.3,wd,ha='center',fontsize=12,bbox=dict(fc='white',ec=INK))
for i in range(4):
    for j in range(4): ax.plot([0.6+i*0.95,0.6+j*0.95],[3.0,1.5],color=RED if j==1 else GREY,lw=2.2 if j==1 else 0.6)
save(fig,'ch7_network_types.png')

# 18 subsumption layers
fig,ax=blank(11,4.8)
layers=[('Layer 3: AVOID','bumper pressed → turn away',RED),('Layer 2: DOCK','battery low → go to charger',AMBER),('Layer 1: WANDER','otherwise → move forward & clean',BLUE)]
for i,(a,b,c) in enumerate(layers):
    y=3.4-i*1.3; box(ax,2.4,y,5.2,1.0,'',fc='white',ec=c); ax.add_patch(Rectangle((2.4,y),0.22,1.0,color=c))
    ax.text(2.85,y+0.65,a,fontsize=13,weight='bold',color=c); ax.text(2.85,y+0.27,b,fontsize=11.5)
    arrow(ax,(1.4,y+0.5),(2.35,y+0.5),c=GREY); arrow(ax,(7.65,y+0.5),(8.6,y+0.5),c=c)
box(ax,0.1,1.3,1.2,2.6,'SENSORS',fc=PALE,bold=True); box(ax,8.7,1.3,2.1,2.6,'MOTORS\n(highest active\nlayer wins)',fc=PALE,bold=True)
ax.text(5,0.15,'higher layers SUBSUME (override) lower ones',ha='center',fontsize=12,style='italic',color=RED)
save(fig,'ch8_subsumption.png')

# 19 RL loop
fig,ax=blank(10,4.6)
box(ax,0.4,1.6,2.6,1.4,'AGENT\n(the learner)',fc='#FDE3DE',ec=RED,bold=True,fs=14)
box(ax,7.0,1.6,2.6,1.4,'ENVIRONMENT\n(the world)',fc='#DCE8FB',ec=BLUE,bold=True,fs=14)
arrow(ax,(3.0,2.8),(7.0,2.8),rad=-0.35,lw=2.4); ax.text(5,4.0,'ACTION  (e.g. mine, move, craft)',ha='center',fontsize=12.5,weight='bold')
arrow(ax,(7.0,1.8),(3.0,1.8),rad=-0.35,lw=2.4); ax.text(5,0.25,'new STATE  +  REWARD (+1 / −1)',ha='center',fontsize=12.5,weight='bold')
ax.text(1.7,1.25,'POLICY = its strategy',ha='center',fontsize=11,style='italic',color=RED)
save(fig,'ch8_rl_loop.png')

# 20 bandit sim
from three_doors_bandit import play
rng=random.Random(42); R=60
res={}
for strat,eps in [('greedy',0),('ε-greedy (ε=0.1)',0.1),('random',1)]:
    curve=np.zeros(R)
    for g in range(2000):
        r_=random.Random(rng.random())
        tot=0
        # replay to get per-round average: use play with growing rounds is costly; simulate inline
        import three_doors_bandit as tdb
        doors=['A','B','C']; T={d:0 for d in doors}; C={d:0 for d in doors}
        for t in range(R):
            un=[d for d in doors if C[d]==0]
            if un: d=un[0]
            elif r_.random()<eps: d=r_.choice(doors)
            else: d=max(doors,key=lambda k:T[k]/C[k])
            rew=tdb.pull(d,r_); T[d]+=rew; C[d]+=1; curve[t]+=rew
    res[strat]=curve/2000
fig,ax=plt.subplots(figsize=(9,4.4))
for (k,v),c in zip(res.items(),[GREY,RED,BLUE]):
    ax.plot(np.arange(3,R-1),np.convolve(v,np.ones(5)/5,mode='valid'),label=k,color=c,lw=2.5)
ax.axhline(1.5,ls='--',color=GREEN); ax.text(R,1.53,'best door (C) = 1.5',ha='right',color=GREEN)
ax.set_xlabel('round'); ax.set_ylabel('average reward per round\n(2,000 simulated players)'); ax.legend(); ax.set_ylim(0.6,1.7)
ax.set_title('Three Doors: a little exploration pays off',fontsize=14,weight='bold')
for k,v in res.items(): print(k, 'last20 avg', v[-20:].mean().round(3))
save(fig,'ch8_bandit_simulation.png')

# 21 q-learning curve + policy
from diamond_hunt_qlearning import train, policy_map, GRID, greedy_path
Q,hist=train()
fig,axs=plt.subplots(1,2,figsize=(13,4.8),gridspec_kw={'width_ratios':[1.4,1]})
axs[0].plot(hist,color=GREY,alpha=0.4,lw=1); axs[0].plot(np.convolve(hist,np.ones(20)/20,mode='valid'),color=RED,lw=2.5,label='20-episode average')
axs[0].set_xlabel('episode (one attempt to reach the diamond)'); axs[0].set_ylabel('total reward'); axs[0].legend(); axs[0].set_title('Diamond Hunt: the agent improves by trial & error',fontsize=13,weight='bold')
ax=axs[1]; ax.set_xlim(0,5); ax.set_ylim(0,5); ax.set_aspect('equal'); ax.axis('off')
pm=policy_map(Q); path=set(greedy_path(Q)); arrows={'>':(0.3,0),'<':(-0.3,0),'^':(0,0.3),'v':(0,-0.3)}
for r in range(5):
    for c in range(5):
        cell=GRID[r][c]; fc={'L':'#F79A3E','D':'#5FD3E8','S':'#FDE3DE'}.get(cell,'#EFE6DA' if (r,c) not in path else '#FFF1B8')
        ax.add_patch(Rectangle((c,4-r),1,1,fc=fc,ec='white',lw=2))
        if cell=='L': ax.text(c+.5,4-r+.5,'LAVA',ha='center',va='center',fontsize=9,weight='bold',color='#8A2B00')
        elif cell=='D': ax.text(c+.5,4-r+.5,'◆',ha='center',va='center',fontsize=26,color='#0A6C80')
        else:
            dx,dy=arrows[pm[r][c]]; ax.annotate('',xy=(c+.5+dx,4-r+.5+dy),xytext=(c+.5-dx,4-r+.5-dy),arrowprops=dict(arrowstyle='-|>',color=INK,lw=2))
ax.text(0.5,4.08,'S',fontsize=10,weight='bold',color=RED); ax.set_title('Learned policy (yellow = path)',fontsize=13,weight='bold')
save(fig,'ch8_qlearning_result.png')

# 22 minecraft-style tech tree (original drawing)
fig,ax=blank(13,3.4)
items=[('wood','#A0703A'),('crafting\ntable','#C08A4A'),('wooden\npickaxe','#C08A4A'),('stone\npickaxe','#8E8E8E'),('iron\npickaxe','#D9D9D9'),('diamond','#5FD3E8')]
for i,(t,c) in enumerate(items):
    x=0.4+i*2.15; ax.add_patch(Rectangle((x,1.2),1.3,1.3,fc=c,ec=INK,lw=2)); ax.text(x+0.65,0.75,t,ha='center',va='top',fontsize=11.5,weight='bold')
    if i<5: arrow(ax,(x+1.35,1.85),(x+2.1,1.85))
ax.text(6.5,3.1,'Sparse reward: the agent only gets the big reward at the END of a long chain of steps',ha='center',fontsize=12,style='italic',color=RED)
save(fig,'ch8_tech_tree.png')
