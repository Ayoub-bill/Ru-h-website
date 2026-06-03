import re

with open('/Users/ayoubesqalli/Documents/GitHub/Rush/rush_homepage_v3.html', 'r') as f:
    html = f.read()

# Remove border-b border-border from all sections and section headers
html = html.replace(' border-b border-border', '')
# Also remove border-r border-border if any are left
html = html.replace(' border-r border-border', '')
# The footer had border-t border-border, let's remove it too to be fully clean, or keep it. Let's remove it.
html = html.replace(' border-t border-border', '')

# Ensure the cards keep their 'border border-border' which we added earlier.
# (The replace above didn't touch 'border border-border', only 'border-b', 'border-t', etc. so it's safe).

# Also remove 'col-span-full ' from the headers since they are no longer in a grid container
html = html.replace('col-span-full ', '')

with open('/Users/ayoubesqalli/Documents/GitHub/Rush/rush_homepage_v3.html', 'w') as f:
    f.write(html)
print("Borders removed successfully.")
