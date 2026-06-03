import re

with open('/Users/ayoubesqalli/Documents/GitHub/Rush/rush_homepage_v3.html', 'r') as f:
    html = f.read()

# Refactor #produits
produits_pattern = r'(<section id="produits" class=")(grid grid-cols-1 lg:grid-cols-3 border-b border-border)(">.*?<div class="col-span-full.*?</p>\n    </div>)\n(.*?</section>)'
def replace_produits(m):
    # Change section class to bg-bg border-b border-border
    new_section_start = m.group(1) + "bg-bg border-b border-border" + m.group(3)
    # The cards are in m.group(4)
    cards = m.group(4)
    # Update card classes: remove border-b lg:border-b-0 lg:border-r border-none lg:border-r-0 border-border
    cards = re.sub(r'border-b lg:border-b-0 lg:border-r border-border', 'border border-border shadow-sm', cards)
    cards = re.sub(r'border-b lg:border-b-0 border-none lg:border-r-0', 'border border-border shadow-sm', cards)
    # Wrap cards in a gap grid
    return new_section_start + '\n    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 p-6 lg:p-10">\n' + cards.replace('</section>', '    </div>\n  </section>')
html = re.sub(produits_pattern, replace_produits, html, flags=re.DOTALL)

# Refactor #pourquoi
pourquoi_pattern = r'(<section id="pourquoi" class=")(grid grid-cols-1 lg:grid-cols-3 border-b border-border)(">.*?<div class="col-span-full.*?</p>\n    </div>)\n(.*?</section>)'
def replace_pourquoi(m):
    new_section_start = m.group(1) + "bg-bg border-b border-border" + m.group(3)
    cards = m.group(4)
    cards = re.sub(r'border-b lg:border-b-0 lg:border-r border-border', 'border border-border shadow-sm', cards)
    cards = re.sub(r'border-b lg:border-b-0 border-r-0 lg:border-r-0', 'border border-border shadow-sm', cards)
    return new_section_start + '\n    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 p-6 lg:p-10">\n' + cards.replace('</section>', '    </div>\n  </section>')
html = re.sub(pourquoi_pattern, replace_pourquoi, html, flags=re.DOTALL)

# Refactor #methode
methode_pattern = r'(<section id="methode" class=")(grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 border-b border-border)(">.*?<div class="col-span-full.*?</h2>\n    </div>)\n(.*?</section>)'
def replace_methode(m):
    new_section_start = m.group(1) + "bg-bg border-b border-border" + m.group(3)
    cards = m.group(4)
    cards = re.sub(r'border-b lg:border-b-0 sm:border-r border-border', 'border border-border shadow-sm', cards)
    cards = re.sub(r'border-b-0 lg:border-b-0 border-r-0', 'border border-border shadow-sm', cards)
    return new_section_start + '\n    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 p-6 lg:p-10">\n' + cards.replace('</section>', '    </div>\n  </section>')
html = re.sub(methode_pattern, replace_methode, html, flags=re.DOTALL)

# Refactor #avis (already has bg-bg and border-b border-border, but needs gap/padding fix)
# We just need to change section padding and add p-6 lg:p-10 to the wrapper
html = html.replace('<section id="avis" class="bg-bg py-14 px-5 border-b border-border">', '<section id="avis" class="bg-bg border-b border-border">')
html = html.replace('<div class="overflow-hidden mt-10">', '<div class="overflow-hidden mt-10 p-6 lg:p-10">')

# Also the .roi-banner - it doesn't have grid-header, but we should space them out as well.
roi_pattern = r'(<section class=")(grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 bg-text text-bg border-b border-border)(">\n)(.*?)(</section>)'
def replace_roi(m):
    cards = m.group(4)
    # Remove borders from ROI items
    cards = re.sub(r'border-b sm:border-b-0 sm:border-r border-border', 'bg-white/5 rounded-2xl shadow-sm', cards)
    # Change section to have gap
    new_section_start = m.group(1) + "bg-text text-bg border-b border-border p-6 lg:p-10" + m.group(3)
    return new_section_start + '  <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">\n' + cards + '  </div>\n' + m.group(5)
html = re.sub(roi_pattern, replace_roi, html, flags=re.DOTALL)

with open('/Users/ayoubesqalli/Documents/GitHub/Rush/rush_homepage_v3.html', 'w') as f:
    f.write(html)
print("Layout fixed successfully.")
