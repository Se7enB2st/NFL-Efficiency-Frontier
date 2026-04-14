import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

GOLD       = '#FFB612'
BLACK      = '#101820'
C_STEAL    = '#1D9E75'
C_ELITE    = '#378ADD'
C_CASUALTY = '#E24B4A'
C_DEV      = '#888780'

# ── MAIN SCATTER ─────────────────────────────────────────────────────────────
data = [
    ('JuJu Smith-Schuster','PIT',2020, 9.75, 0.225,True),
    ('Diontae Johnson',    'PIT',2020, 0.78, 0.109,True),
    ('Chase Claypool',     'PIT',2020, 0.78, 0.410,True),
    ('Davante Adams',      'GB', 2020,14.50, 0.389,False),
    ('Tyreek Hill',        'KC', 2020,15.38, 0.341,False),
    ('DK Metcalf',         'SEA',2020, 0.92, 0.388,False),
    ('Justin Jefferson',   'MIN',2020, 0.87, 0.298,False),
    ('Allen Robinson',     'CHI',2020,14.00, 0.201,False),
    ("Ja'Marr Chase",      'CIN',2021, 0.87, 0.493,False),
    ('Cooper Kupp',        'LAR',2021, 9.50, 0.441,False),
    ('Diontae Johnson',    'PIT',2021, 1.84, 0.066,True),
    ('Chase Claypool',     'PIT',2021, 0.82, 0.074,True),
    ('JuJu Smith-Schuster','PIT',2021, 4.00,-0.235,True),
    ('Davante Adams',      'GB', 2021,16.50, 0.398,False),
    ('Allen Robinson',     'CHI',2021,14.00, 0.051,False),
    ('George Pickens',     'PIT',2022, 0.78, 0.534,True),
    ('Diontae Johnson',    'PIT',2022, 8.50,-0.008,True),
    ('Chase Claypool',     'PIT',2022, 0.81,-0.075,True),
    ("Ja'Marr Chase",      'CIN',2022, 3.21, 0.303,False),
    ('Justin Jefferson',   'MIN',2022, 3.42, 0.441,False),
    ('Tyreek Hill',        'MIA',2022,26.50, 0.388,False),
    ('Davante Adams',      'LV', 2022,28.00, 0.398,False),
    ('Allen Robinson',     'LAR',2022,18.00, 0.041,False),
    ('George Pickens',     'PIT',2023, 0.79, 0.184,True),
    ('Diontae Johnson',    'PIT',2023, 8.50, 0.333,True),
    ('Calvin Austin III',  'PIT',2023, 1.00,-0.042,True),
    ("Ja'Marr Chase",      'CIN',2023, 9.53, 0.418,False),
    ('Tyreek Hill',        'MIA',2023,26.50, 0.412,False),
    ('CeeDee Lamb',        'DAL',2023, 3.42, 0.501,False),
    ('George Pickens',     'PIT',2024, 1.05, 0.336,True),
    ('Calvin Austin III',  'PIT',2024, 1.10, 0.410,True),
    ('Mike Williams',      'PIT',2024, 1.10, 0.477,True),
    ("Ja'Marr Chase",      'CIN',2024,11.10, 0.440,False),
    ('Justin Jefferson',   'MIN',2024,12.25, 0.398,False),
    ('Tyreek Hill',        'MIA',2024,27.70, 0.191,False),
    ('DK Metcalf',         'PIT',2025,11.00, 0.320,True),
    ('Calvin Austin III',  'PIT',2025, 2.20,-0.094,True),
    ('Roman Wilson',       'PIT',2025, 0.94, 0.194,True),
    ('Puka Nacua',         'LAR',2025, 2.10, 0.512,False),
    ("Ja'Marr Chase",      'CIN',2025,23.12, 0.224,False),
    ('Amon-Ra St. Brown',  'DET',2025,13.91, 0.341,False),
    ('Tyreek Hill',        'MIA',2025,27.70, 0.081,False),
    ('Michael Pittman Jr', 'IND',2025,23.01, 0.148,False),
    ('CeeDee Lamb',        'DAL',2025,15.34, 0.354,False),
    ('AJ Brown',           'PHI',2025,17.52, 0.341,False),
]

caps   = [d[3] for d in data]
epas   = [d[4] for d in data]
is_pit = [d[5] for d in data]
names  = [d[0] for d in data]
years  = [d[2] for d in data]

def cluster(cap, epa):
    if cap > 12 and epa > 0.25:  return 'Elite Earner'
    if cap <= 12 and epa > 0.20: return 'Efficient Steal'
    if cap > 12 and epa <= 0.25: return 'Cap Casualty'
    return 'Developmental'

clusters = [cluster(c,e) for c,e in zip(caps,epas)]
cmap = {'Elite Earner':C_ELITE,'Efficient Steal':C_STEAL,'Cap Casualty':C_CASUALTY,'Developmental':C_DEV}

fig, ax = plt.subplots(figsize=(8.5, 5.0))
fig.patch.set_facecolor('white')
ax.set_facecolor('#FAFAFA')

for cap, epa, cl, pit in zip(caps, epas, clusters, is_pit):
    ax.scatter(cap, epa, c=cmap[cl],
               s=65 if pit else 38,
               marker='D' if pit else 'o',
               edgecolors=GOLD if pit else 'white',
               linewidths=1.8 if pit else 0.5,
               alpha=0.92, zorder=5 if pit else 3)

annots = {
    ('George Pickens',2022): ( 0.6, 0.09,'Pickens 2022\n$0.78M  EPA 0.53'),
    ('Diontae Johnson',2022):( 1.4,-0.10,'D.Johnson 2022\n$8.5M  EPA -0.01'),
    ('DK Metcalf',2025):     ( 0.7, 0.07,'Metcalf 2025\n$11M  EPA 0.32'),
    ('Mike Williams',2024):  (-5.0, 0.07,'Williams 2024\n$1.1M  EPA 0.48'),
    ('Michael Pittman Jr',2025):( 0.5,-0.12,'Pittman 2025\n$23M  EPA 0.15'),
}
for name,yr,cap,epa in zip(names,years,caps,epas):
    if (name,yr) in annots:
        dx,dy,lbl = annots[(name,yr)]
        ax.annotate(lbl, xy=(cap,epa), xytext=(cap+dx,epa+dy),
            fontsize=6.5, color='#222',
            arrowprops=dict(arrowstyle='->',color='#888',lw=0.8),
            bbox=dict(boxstyle='round,pad=0.2',fc='white',ec='#ccc',lw=0.5),zorder=10)

ax.axhline(0.25,color='#bbb',lw=0.8,ls='--')
ax.axvline(12,  color='#bbb',lw=0.8,ls='--')
ax.text(12.2,-0.38,'$12M threshold',fontsize=7,color='#999')
ax.text(0.3, 0.26, 'EPA 0.25',fontsize=7,color='#999')
ax.set_xlabel('Cap Hit ($M)',fontsize=10,labelpad=5)
ax.set_ylabel('EPA per Target',fontsize=10,labelpad=5)
ax.set_xlim(-1,31); ax.set_ylim(-0.42,0.66)
ax.tick_params(labelsize=8)
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x,_: f'${x:.0f}M'))
ax.grid(True,alpha=0.22,lw=0.5)
ax.spines[['top','right']].set_visible(False)
leg = [
    mpatches.Patch(fc=C_STEAL,   ec='white',label='Efficient Steal'),
    mpatches.Patch(fc=C_ELITE,   ec='white',label='Elite Earner'),
    mpatches.Patch(fc=C_CASUALTY,ec='white',label='Cap Casualty'),
    mpatches.Patch(fc=C_DEV,     ec='white',label='Developmental'),
    plt.scatter([],[],marker='D',c='gray',edgecolors=GOLD,linewidths=1.8,s=55,label='Steelers'),
]
ax.legend(handles=leg,fontsize=7.5,loc='upper right',framealpha=0.9,edgecolor='#ddd')
plt.tight_layout(pad=0.5)
fig.savefig('fig_scatter.png',dpi=180,bbox_inches='tight',facecolor='white')
plt.close()
print('scatter done')

# ── TRAJECTORY LINE CHART ─────────────────────────────────────────────────
players = {
    'Diontae Johnson': {
        2020:(0.78,0.109), 2021:(1.84,0.066), 2022:(8.50,-0.008), 2023:(8.50,0.333)
    },
    'George Pickens': {
        2022:(0.78,0.534), 2023:(0.79,0.184), 2024:(1.05,0.336)
    },
    'Chase Claypool': {
        2020:(0.78,0.410), 2021:(0.82,0.074), 2022:(0.81,-0.075)
    },
}
league_avg = {2020:0.310,2021:0.315,2022:0.308,2023:0.312,2024:0.309,2025:0.310}
pit_avg    = {2020:0.248,2021:0.088,2022:0.150,2023:0.163,2024:0.408,2025:0.140}

colors_p  = {'Diontae Johnson':'#E24B4A','George Pickens':'#1D9E75','Chase Claypool':'#7F77DD'}
markers_p = {'Diontae Johnson':'s','George Pickens':'D','Chase Claypool':'^'}

fig2, ax2 = plt.subplots(figsize=(8.0, 3.6))
fig2.patch.set_facecolor('white')
ax2.set_facecolor('#FAFAFA')

yrs_lg = sorted(league_avg.keys())
ax2.plot(yrs_lg,[league_avg[y] for y in yrs_lg],color='#BBBBBB',lw=1.5,
         ls='--',label='League avg',zorder=1)
yrs_pit = sorted(pit_avg.keys())
ax2.plot(yrs_pit,[pit_avg[y] for y in yrs_pit],color='#B8860B',lw=2.5,
         ls='-',marker='o',ms=7,label='PIT room avg',zorder=3)

for pname, seasons in players.items():
    xs = sorted(seasons.keys())
    ys = [seasons[x][1] for x in xs]
    ax2.plot(xs, ys, color=colors_p[pname], lw=2, marker=markers_p[pname],
             ms=8, label=pname, zorder=4)
    for x,y in zip(xs,ys):
        cap = seasons[x][0]
        if cap > 4:
            ax2.annotate(f'${cap:.0f}M', xy=(x,y),
                xytext=(0,10), textcoords='offset points',
                fontsize=6.5, ha='center', color=colors_p[pname])

ax2.set_xlabel('Season', fontsize=9)
ax2.set_ylabel('EPA per Target', fontsize=9)
ax2.set_xticks([2020,2021,2022,2023,2024,2025])
ax2.set_ylim(-0.22, 0.68)
ax2.grid(True,alpha=0.22,lw=0.5)
ax2.spines[['top','right']].set_visible(False)
ax2.tick_params(labelsize=8)
ax2.legend(fontsize=7.5, loc='upper right', framealpha=0.9, edgecolor='#ddd', ncol=2)
plt.tight_layout(pad=0.5)
fig2.savefig('fig_trajectory.png',dpi=180,bbox_inches='tight',facecolor='white')
plt.close()
print('trajectory done')
