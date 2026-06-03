import re

# We will read the file
with open('/Users/ayoubesqalli/Documents/GitHub/Rush/rush_homepage_v3.html', 'r') as f:
    content = f.read()

# 1. Add Tailwind CDN in <head>
tailwind_cdn = """
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      darkMode: ['class', '[data-theme="dark"]'],
      theme: {
        extend: {
          colors: {
            orange: 'var(--orange)',
            'orange-hover': 'var(--orange-hover)',
            bg: 'var(--bg)',
            surface: 'var(--surface)',
            text: 'var(--text)',
            border: 'var(--border)',
            muted: 'var(--muted)',
            'surface-hover': 'var(--surface-hover)',
          },
          fontFamily: {
            sans: ['var(--app-font)', 'sans-serif'],
          }
        }
      }
    }
  </script>
"""

content = content.replace('</title>', '</title>\n' + tailwind_cdn)

# 2. Modify body class
content = content.replace('<body>', '<body class="bg-bg text-text font-sans text-[length:var(--app-font-size)] font-medium antialiased transition-colors duration-150">')

# 3. Replace <style> block with ONLY the CSS variables and keyframes
style_block_pattern = re.compile(r'<style>.*?</style>', re.DOTALL)

essential_css = """<style type="text/tailwindcss">
    @layer base {
      :root {
        --orange: #FF3D00;
        --orange-hover: color-mix(in srgb, var(--orange) 85%, black);
        --bg: #F9F9F9;
        --surface: #FFFFFF;
        --text: #1A1A1A;
        --border: #E5E5E5;
        --muted: #666666;
        --logo-invert: 0;
        --surface-hover: #F0F0F0;
        --app-font: 'Futura', 'Jost', sans-serif;
        --app-font-size: 16px;
        --app-font-weight: 700;
        --app-radius: 8px;
        --app-shadow: 4px;
      }
      [data-theme="dark"] {
        --bg: #0A0A0A;
        --surface: #141414;
        --text: #FFFFFF;
        --border: #333333;
        --muted: #999999;
        --logo-invert: 1;
        --surface-hover: #1E1E1E;
      }
      
      h1, h2, h3, .impact-text {
        @apply uppercase italic font-[var(--app-font-weight)] tracking-tight leading-none;
      }
      
      [data-theme="dark"] .nav-logo img,
      [data-theme="dark"] .footer-logo img {
        filter: brightness(0) invert(1);
      }
    }

    /* We can still keep complex hover effects and pseudo-elements here if Tailwind arbitrary values are too long, but let's try to map them directly. We'll keep the keyframes. */
    @keyframes scrollReviews {
      0% { transform: translateX(0); }
      100% { transform: translateX(-50%); }
    }
    @keyframes pulse {
      0% { box-shadow: 0 0 0 0 rgba(46,204,113,0.4); }
      70% { box-shadow: 0 0 0 8px rgba(46,204,113,0); }
      100% { box-shadow: 0 0 0 0 rgba(46,204,113,0); }
    }

    /* Keep complex product-card backgrounds */
    .product-card::before {
      content: '';
      position: absolute;
      inset: 0;
      background-size: cover;
      background-position: center;
      background-repeat: no-repeat;
      opacity: 0;
      transition: opacity 0.4s cubic-bezier(0.25, 1, 0.5, 1);
      z-index: 0;
    }
    .product-card::after {
      content: '';
      position: absolute;
      inset: 0;
      background: linear-gradient(to top, rgba(0,0,0,0.85) 0%, rgba(0,0,0,0.5) 50%, rgba(0,0,0,0.3) 100%);
      opacity: 0;
      transition: opacity 0.4s cubic-bezier(0.25, 1, 0.5, 1);
      z-index: 1;
    }
    .product-card:hover::before, .product-card:hover::after { opacity: 1; }
    .product-card > * { position: relative; z-index: 2; }
    .product-card:hover .product-num, .product-card:hover h3, .product-card:hover p { color: #FFFFFF; }
    .product-card:hover .product-num { color: var(--orange); }
    .product-card--borne::before { background-image: url('./modules/Borne.jpg'); }
    .product-card--webapp::before { background-image: url('./modules/webapp.jpg'); }
    .product-card--fidelite::before { background-image: url('./modules/fidélité.jpg'); }

    /* CTA overlay */
    .cta-section::before {
      content: '';
      position: absolute;
      inset: 0;
      background: rgba(0, 0, 0, 0.55);
      z-index: 1;
    }
    .cta-section > * {
      position: relative;
      z-index: 2;
    }
    .accent-highlight::before {
      content: '';
      position: absolute;
      inset: -4px -12px;
      background: var(--orange);
      z-index: -1;
      transform: skewX(-4deg);
    }
  </style>"""

content = style_block_pattern.sub(essential_css, content)

# 4. Global class replacements via Regex to inject Tailwind classes
mappings = [
    (r'class="banner"', r'class="bg-text text-bg text-center py-3 px-5 text-xs font-bold uppercase tracking-wider transition-colors duration-150"'),
    (r'class="highlight"', r'class="text-orange"'),
    (r'<nav>', r'<nav class="sticky top-0 z-50 bg-surface border-b border-border px-5 lg:px-10 h-[72px] flex items-center justify-between transition-colors duration-150">'),
    (r'class="nav-logo"', r'class="nav-logo flex items-center justify-center h-full w-[120px] overflow-hidden relative"'),
    (r'alt="RU\$H" />\s*</a>', r'alt="RU$H" class="absolute h-[100px] w-auto top-1/2 left-1/2 -translate-x-[52%] -translate-y-1/2 max-w-none transition-all duration-150" />\n    </a>'),
    (r'class="nav-links"', r'class="hidden sm:flex gap-8"'),
    (r'<ul class="hidden sm:flex gap-8">\s*<li><a href="#produits">', r'<ul class="hidden sm:flex gap-8">\n      <li><a href="#produits" class="text-[13px] font-bold uppercase tracking-widest text-text transition-colors duration-100 hover:text-orange">'),
    (r'<li><a href="#avis">', r'<li><a href="#avis" class="text-[13px] font-bold uppercase tracking-widest text-text transition-colors duration-100 hover:text-orange">'),
    (r'<li><a href="#contact">', r'<li><a href="#contact" class="text-[13px] font-bold uppercase tracking-widest text-text transition-colors duration-100 hover:text-orange">'),
    (r'class="nav-cta"', r'class="flex gap-3 items-center"'),
    (r'class="theme-toggle"', r'class="theme-toggle bg-transparent border border-border text-text w-10 h-10 flex items-center justify-center text-base cursor-pointer transition-colors duration-150 hover:bg-text hover:text-surface rounded"'),
    (r'class="btn-primary"', r'class="btn-primary inline-block text-[length:calc(var(--app-font-size)*0.875)] font-[var(--app-font-weight)] uppercase tracking-wide text-white bg-orange border border-orange px-7 py-3.5 rounded-[var(--app-radius)] cursor-pointer transition-all duration-100 hover:bg-orange-hover hover:border-orange-hover hover:-translate-y-0.5 hover:shadow-[0_var(--app-shadow)_calc(var(--app-shadow)*3)_color-mix(in_srgb,var(--orange)_30%,transparent)]"'),
    (r'class="btn-ghost"', r'class="btn-ghost inline-block text-[length:calc(var(--app-font-size)*0.875)] font-[var(--app-font-weight)] uppercase tracking-wide text-text bg-transparent border border-text px-7 py-3.5 rounded-[var(--app-radius)] cursor-pointer transition-all duration-100 hover:bg-text hover:text-surface hover:-translate-y-0.5 hover:shadow-[0_var(--app-shadow)_calc(var(--app-shadow)*3)_color-mix(in_srgb,var(--orange)_30%,transparent)]"'),
    (r'class="hero"', r'class="grid grid-cols-1 lg:grid-cols-2 border-b border-border"'),
    (r'class="hero-content"', r'class="bg-surface px-6 py-15 lg:py-25 lg:px-15 flex flex-col justify-center border-b lg:border-b-0 lg:border-r border-border transition-colors duration-150"'),
    (r'class="hero-tag"', r'class="text-xs font-bold uppercase text-muted tracking-widest mb-8"'),
    (r'<h1>', r'<h1 class="text-[clamp(48px,6vw,80px)] leading-[0.9] mb-7 font-extrabold">'),
    (r'class="accent"', r'class="text-orange"'),
    (r'class="hero-desc"', r'class="text-[17px] text-muted font-medium mb-12 max-w-[440px] leading-relaxed"'),
    (r'class="hero-image"', r'class="bg-surface overflow-hidden relative min-h-[300px] lg:min-h-[520px] transition-colors duration-150"'),
    (r'alt="Borne de commande RU\$H en action dans un fast-food" />', r'alt="Borne de commande RU$H en action dans un fast-food" class="w-full h-full object-cover absolute inset-0" />'),
    (r'class="logos-bar"', r'class="py-12 px-10 bg-bg border-b border-border text-center transition-colors duration-150"'),
    (r'<p>Ils font confiance à Rush</p>', r'<p class="text-[11px] font-bold uppercase text-muted tracking-widest mb-7">Ils font confiance à Rush</p>'),
    (r'class="logos-row"', r'class="logos-row flex justify-center items-center gap-12 flex-wrap"'),
    (r'alt="Burger King" />', r'alt="Burger King" class="h-9 w-auto object-contain opacity-60 hover:opacity-100 transition-opacity duration-150" />'),
    (r'alt="Burger\'s" />', r'alt="Burger\'s" class="h-9 w-auto object-contain opacity-60 hover:opacity-100 transition-opacity duration-150" />'),
    (r'alt="GOMU" />', r'alt="GOMU" class="h-9 w-auto object-contain opacity-60 hover:opacity-100 transition-opacity duration-150" />'),
    (r'alt="Green 2 Green" />', r'alt="Green 2 Green" class="h-9 w-auto object-contain opacity-60 hover:opacity-100 transition-opacity duration-150" />'),
    (r'class="products-grid"', r'class="grid grid-cols-1 lg:grid-cols-3 border-b border-border"'),
    (r'class="grid-header"', r'class="col-span-full py-15 px-6 lg:py-20 lg:px-15 lg:pb-12 bg-surface border-b border-border transition-colors duration-150"'),
    (r'<h2>', r'<h2 class="text-[clamp(36px,4vw,52px)] leading-[0.95]">'),
    (r'class="subtitle"', r'class="text-[17px] mt-5 text-muted max-w-[560px] font-medium leading-relaxed"'),
    (r'class="product-card product-card--borne"', r'class="product-card product-card--borne p-10 lg:p-14 border-b lg:border-b-0 lg:border-r border-border bg-surface rounded-[calc(var(--app-radius)*2)] transition-colors duration-150 relative overflow-hidden group hover:bg-surface"'),
    (r'class="product-card product-card--webapp"', r'class="product-card product-card--webapp p-10 lg:p-14 border-b lg:border-b-0 lg:border-r border-border bg-surface rounded-[calc(var(--app-radius)*2)] transition-colors duration-150 relative overflow-hidden group hover:bg-surface"'),
    (r'class="product-card product-card--fidelite" style="border-right: none;"', r'class="product-card product-card--fidelite p-10 lg:p-14 border-b lg:border-b-0 border-none lg:border-r-0 bg-surface rounded-[calc(var(--app-radius)*2)] transition-colors duration-150 relative overflow-hidden group hover:bg-surface"'),
    (r'class="product-num"', r'class="product-num text-[56px] font-[var(--app-font-weight)] italic text-orange leading-none mb-6 transition-colors duration-300 group-hover:text-orange"'),
    (r'<h3>Borne de commande</h3>', r'<h3 class="text-[26px] leading-none mb-4 transition-colors duration-300 group-hover:text-white">Borne de commande</h3>'),
    (r'<p>Vos clients commandent seuls', r'<p class="text-[15px] text-muted leading-relaxed font-normal transition-colors duration-300 group-hover:text-white">Vos clients commandent seuls'),
    (r'<h3>Web App</h3>', r'<h3 class="text-[26px] leading-none mb-4 transition-colors duration-300 group-hover:text-white">Web App</h3>'),
    (r'<p>Click & Collect', r'<p class="text-[15px] text-muted leading-relaxed font-normal transition-colors duration-300 group-hover:text-white">Click & Collect'),
    (r'<h3>Fidélité</h3>', r'<h3 class="text-[26px] leading-none mb-4 transition-colors duration-300 group-hover:text-white">Fidélité</h3>'),
    (r'<p>Points, récompenses', r'<p class="text-[15px] text-muted leading-relaxed font-normal transition-colors duration-300 group-hover:text-white">Points, récompenses'),
    (r'class="section-grid col-3"', r'class="grid grid-cols-1 lg:grid-cols-3 border-b border-border"'),
    (r'class="bento-box"', r'class="bento-box p-10 lg:p-14 bg-surface rounded-[calc(var(--app-radius)*2)] transition-colors duration-150 relative border-b lg:border-b-0 lg:border-r border-border hover:bg-surface-hover"'),
    (r'class="bento-box no-right-border"', r'class="bento-box p-10 lg:p-14 bg-surface rounded-[calc(var(--app-radius)*2)] transition-colors duration-150 relative border-b lg:border-b-0 border-r-0 lg:border-r-0 hover:bg-surface-hover"'),
    (r'class="bento-box span-2"', r'class="bento-box col-span-1 lg:col-span-2 p-10 lg:p-14 bg-surface rounded-[calc(var(--app-radius)*2)] transition-colors duration-150 relative border-b lg:border-b-0 lg:border-r border-border hover:bg-surface-hover"'),
    (r'class="box-icon"', r'class="text-[28px] mb-6 block leading-none"'),
    (r'<h3>Compris', r'<h3 class="text-[24px] leading-none mb-4">Compris'),
    (r'<h3>Opérationnel', r'<h3 class="text-[24px] leading-none mb-4">Opérationnel'),
    (r'<h3>Rentable', r'<h3 class="text-[24px] leading-none mb-4">Rentable'),
    (r'<h3>La puissance', r'<h3 class="text-[24px] leading-none mb-4">La puissance'),
    (r'<h3>Un humain', r'<h3 class="text-[24px] leading-none mb-4">Un humain'),
    (r'<h3>On échange', r'<h3 class="text-[24px] leading-none mb-4">On échange'),
    (r'<h3>On configure', r'<h3 class="text-[24px] leading-none mb-4">On configure'),
    (r'<h3>On installe', r'<h3 class="text-[24px] leading-none mb-4">On installe'),
    (r'<h3>Vous encaissez', r'<h3 class="text-[24px] leading-none mb-4">Vous encaissez'),
    (r'<p>Une offre claire', r'<p class="text-[15px] text-muted leading-relaxed font-normal">Une offre claire'),
    (r'<p>Votre borne encaisse', r'<p class="text-[15px] text-muted leading-relaxed font-normal">Votre borne encaisse'),
    (r'<p>Un tarif transparent', r'<p class="text-[15px] text-muted leading-relaxed font-normal">Un tarif transparent'),
    (r'<p>Des années', r'<p class="text-[15px] text-muted leading-relaxed font-normal">Des années'),
    (r'<p>Un interlocuteur', r'<p class="text-[15px] text-muted leading-relaxed font-normal">Un interlocuteur'),
    (r'<p>30 minutes', r'<p class="text-[15px] text-muted leading-relaxed font-normal">30 minutes'),
    (r'<p>Votre menu', r'<p class="text-[15px] text-muted leading-relaxed font-normal">Votre menu'),
    (r'<p>Livraison', r'<p class="text-[15px] text-muted leading-relaxed font-normal">Livraison'),
    (r'<p>Votre borne tourne.', r'<p class="text-[15px] text-muted leading-relaxed font-normal">Votre borne tourne.'),
    (r'class="section-grid col-4"', r'class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 border-b border-border"'),
    (r'class="bento-box no-bottom-border"', r'class="bento-box p-10 lg:p-14 bg-surface rounded-[calc(var(--app-radius)*2)] transition-colors duration-150 relative border-b lg:border-b-0 sm:border-r border-border hover:bg-surface-hover"'),
    (r'class="bento-box no-right-border no-bottom-border"', r'class="bento-box p-10 lg:p-14 bg-surface rounded-[calc(var(--app-radius)*2)] transition-colors duration-150 relative border-b-0 lg:border-b-0 border-r-0 hover:bg-surface-hover"'),
    (r'class="roi-banner"', r'class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 bg-text text-bg border-b border-border"'),
    (r'class="roi-item"', r'class="p-10 lg:p-15 border-b sm:border-b-0 sm:border-r border-border transition-colors duration-150 hover:bg-white/5"'),
    (r'class="roi-num"', r'class="font-[var(--app-font-weight)] text-[clamp(48px,5vw,68px)] leading-none text-orange italic mb-5"'),
    (r'class="roi-num" style="margin-bottom: 20px;"', r'class="font-[var(--app-font-weight)] text-[clamp(48px,5vw,68px)] leading-none text-orange italic mb-5"'),
    (r'class="roi-label"', r'class="text-[13px] uppercase font-bold tracking-widest mt-3 opacity-70"'),
    (r'class="reviews-section"', r'class="bg-bg py-14 px-5 border-b border-border"'),
    (r'class="reviews-carousel"', r'class="overflow-hidden mt-10"'),
    (r'class="reviews-track"', r'class="flex gap-5 items-stretch animate-[scrollReviews_22s_linear_infinite]"'),
    (r'class="review-card"', r'class="bg-surface p-5 min-w-[300px] rounded-[calc(var(--app-radius)*1.5)] shadow-[0_calc(var(--app-shadow)*1.5)_calc(var(--app-shadow)*4.5)_rgba(0,0,0,0.06)] flex gap-3.5 items-start"'),
    (r'class="avatar"', r'class="w-16 h-16 rounded-full object-cover shrink-0"'),
    (r'class="review-content"', r'class="flex-1"'),
    (r'class="stars"', r'class="text-[#FFD700] mb-2 text-sm"'),
    (r'<p>"La borne', r'<p class="text-[15px] italic text-muted mb-2">"La borne'),
    (r'<p>"Installation', r'<p class="text-[15px] italic text-muted mb-2">"Installation'),
    (r'<p>"Support', r'<p class="text-[15px] italic text-muted mb-2">"Support'),
    (r'<strong>', r'<strong class="text-xs uppercase font-bold tracking-wider text-text">'),
    (r'class="pricing-section"', r'class="py-16 px-5 bg-surface text-center border-b border-border"'),
    (r'class="pricing-card"', r'class="max-w-[720px] mx-auto p-8 rounded-[calc(var(--app-radius)*2)] border-2 border-orange/10 shadow-[0_calc(var(--app-shadow)*2.5)_calc(var(--app-shadow)*7.5)_rgba(0,0,0,0.04)]"'),
    (r'<h3>RU\$H — Pack Standard</h3>', r'<h3 class="text-[24px] font-bold mb-3">RU$H — Pack Standard</h3>'),
    (r'<p>Une solution complète', r'<p class="text-[15px] text-muted mb-5">Une solution complète'),
    (r'class="pricing-list"', r'class="list-none p-0 mt-5 mx-auto max-w-[300px] text-left"'),
    (r'<li><i', r'<li class="flex gap-3 items-center py-2"><i'),
    (r'fa-check-circle"></i>', r'fa-check-circle text-[#2ECC71] text-lg"></i>'),
    (r'class="contact-section"', r'class="py-10 px-5 bg-bg"'),
    (r'class="contact-card"', r'class="max-w-[720px] mx-auto bg-surface p-5 rounded-[calc(var(--app-radius)*1.5)] border border-border mt-8"'),
    (r'input type="text"', r'input type="text" class="w-full px-4 py-3 border border-[#CCC] rounded-[var(--app-radius)] text-[15px] mb-3 transition-colors duration-150 focus:outline-none focus:border-orange focus:shadow-[0_calc(var(--app-shadow)*1.5)_calc(var(--app-shadow)*4.5)_color-mix(in_srgb,var(--orange)_8%,transparent)] bg-transparent text-text"'),
    (r'input type="email"', r'input type="email" class="w-full px-4 py-3 border border-[#CCC] rounded-[var(--app-radius)] text-[15px] mb-3 transition-colors duration-150 focus:outline-none focus:border-orange focus:shadow-[0_calc(var(--app-shadow)*1.5)_calc(var(--app-shadow)*4.5)_color-mix(in_srgb,var(--orange)_8%,transparent)] bg-transparent text-text"'),
    (r'<textarea name="message"', r'<textarea name="message" class="w-full px-4 py-3 border border-[#CCC] rounded-[var(--app-radius)] text-[15px] mb-3 transition-colors duration-150 focus:outline-none focus:border-orange focus:shadow-[0_calc(var(--app-shadow)*1.5)_calc(var(--app-shadow)*4.5)_color-mix(in_srgb,var(--orange)_8%,transparent)] bg-transparent text-text"'),
    (r'class="online-badge"', r'class="flex items-center gap-2 mt-2"'),
    (r'class="online-dot"', r'class="w-2.5 h-2.5 bg-[#2ECC71] rounded-full animate-[pulse_2s_infinite]"'),
    (r'class="cta-section"', r'class="cta-section py-24 lg:py-32 px-6 lg:px-10 text-center border-b border-border relative overflow-hidden bg-[url(\'./Rush-gradient-bg.jpg\')] bg-cover bg-center"'),
    (r'<h2>', r'<h2 class="text-[clamp(40px,5vw,72px)] leading-[0.95] mb-6 text-white">'),
    (r'class="accent-highlight"', r'class="accent-highlight text-white relative inline-block px-3 mx-1"'),
    (r'<p class="text-\[17px\]', r'<p class="text-[17px] text-white/85 max-w-[480px] mx-auto mb-12 font-medium leading-relaxed'),
    (r'class="cta-buttons"', r'class="flex gap-4 justify-center flex-wrap"'),
    (r'<footer>', r'<footer class="bg-bg py-15 px-10 flex flex-col sm:flex-row justify-between sm:items-end gap-10 sm:gap-0 border-t border-border transition-colors duration-150">'),
    (r'class="footer-logo"', r'class="flex flex-col gap-2.5"'),
    (r'class="footer-logo-wrap"', r'class="w-[100px] h-9 overflow-hidden relative"'),
    (r'alt="RU\$H" />\n      </div>', r'alt="RU$H" class="absolute h-[90px] w-auto top-1/2 left-1/2 -translate-x-[52%] -translate-y-1/2 max-w-none" />\n      </div>'),
    (r'class="footer-powered"', r'class="text-[11px] font-bold text-muted uppercase tracking-widest"'),
    (r'class="footer-links"', r'class="flex gap-10"'),
    (r'class="footer-links">\s*<a href="#">Légal</a>', r'class="flex gap-10">\n      <a href="#" class="text-text font-bold text-[13px] uppercase tracking-widest transition-colors duration-100 hover:text-orange">Légal</a>'),
    (r'<a href="#">CGU</a>', r'<a href="#" class="text-text font-bold text-[13px] uppercase tracking-widest transition-colors duration-100 hover:text-orange">CGU</a>'),
    (r'<a href="#">Contact</a>\s*</div>', r'<a href="#" class="text-text font-bold text-[13px] uppercase tracking-widest transition-colors duration-100 hover:text-orange">Contact</a>\n    </div>'),
]

for pattern, repl in mappings:
    content = re.sub(pattern, repl, content)

# 5. Extract Customizer and Wrap in Slide-over
# Let's extract the `.customizer-section`
customizer_match = re.search(r'<!-- ═══════════════ DESIGN CUSTOMIZER ═══════════════ -->.*?<section class="customizer-section">.*?</section>', content, re.DOTALL)
if customizer_match:
    customizer_html = customizer_match.group(0)
    
    # Remove from original location
    content = content.replace(customizer_html, '')
    
    # Create the slide-over HTML
    # We will format the customizer itself with Tailwind
    customizer_tw = customizer_html.replace('class="customizer-section"', 'class="h-full bg-surface p-6 flex flex-col"')
    customizer_tw = customizer_tw.replace('class="customizer-header"', 'class="text-center mb-8"')
    customizer_tw = customizer_tw.replace('class="customizer-grid"', 'class="flex flex-col gap-4 overflow-y-auto"')
    customizer_tw = customizer_tw.replace('class="customizer-group"', 'class="bg-bg p-4 rounded-[10px] border border-border"')
    customizer_tw = customizer_tw.replace('<label ', '<label class="block text-xs font-bold uppercase tracking-wide mb-2 text-text" ')
    customizer_tw = customizer_tw.replace('<select ', '<select class="w-full p-2 border border-border rounded-md text-[13px] cursor-pointer bg-surface text-text" ')
    customizer_tw = customizer_tw.replace('<input type="color"', '<input type="color" class="w-full h-10 p-1 border border-border rounded-md cursor-pointer bg-surface" ')
    customizer_tw = customizer_tw.replace('<input type="range"', '<input type="range" class="w-full cursor-pointer" ')
    customizer_tw = customizer_tw.replace('class="value-display"', 'class="text-[11px] text-muted mt-1.5 font-medium"')
    customizer_tw = customizer_tw.replace('class="customizer-preview"', 'class="mt-4 text-center p-5 bg-bg rounded-[10px] flex justify-center items-center gap-3"')
    customizer_tw = customizer_tw.replace('class="preview-btn"', 'class="preview-btn inline-block px-6 py-3 bg-orange text-white border-none rounded-[var(--app-radius)] font-[var(--app-font)] text-[length:calc(var(--app-font-size)*0.875)] font-[var(--app-font-weight)] cursor-pointer transition-all duration-150 uppercase hover:-translate-y-0.5 hover:shadow-[0_var(--app-shadow)_calc(var(--app-shadow)*3)_color-mix(in_srgb,var(--orange)_30%,transparent)]"')
    customizer_tw = customizer_tw.replace('class="preview-text"', 'class="text-xs text-muted italic"')
    customizer_tw = customizer_tw.replace('class="customizer-reset"', 'class="mt-4 text-center pb-10"')
    customizer_tw = customizer_tw.replace('<button id="resetBtn">', '<button id="resetBtn" class="px-4 py-2 bg-text text-surface border border-text rounded-md text-xs font-bold cursor-pointer transition-opacity duration-150 uppercase hover:opacity-80">')
    
    # We will add a close button to the header
    customizer_tw = customizer_tw.replace('<h3>🎨 Design Customizer</h3>', '<div class="flex justify-between items-center mb-2"><h3 class="text-xl m-0">🎨 Design Customizer</h3><button onclick="closeCustomizer()" class="text-text hover:text-orange bg-transparent border-none text-xl cursor-pointer"><i class="fa-solid fa-times"></i></button></div>')
    
    slide_over_container = f"""
  <!-- ═══════════════ SLIDE OVER CUSTOMIZER ═══════════════ -->
  <button onclick="openCustomizer()" class="fixed top-1/2 right-0 -translate-y-1/2 z-[90] p-3 bg-orange text-white rounded-l-lg shadow-lg hover:pr-5 transition-all duration-300 cursor-pointer" aria-label="Ouvrir le Customizer">
    <i class="fa-solid fa-palette text-xl"></i>
  </button>

  <div id="customizer-backdrop" class="fixed inset-0 bg-black/50 z-[95] hidden opacity-0 transition-opacity duration-300" onclick="closeCustomizer()"></div>
  
  <div id="customizer-panel" class="fixed top-0 right-0 h-full w-80 max-w-full bg-surface shadow-2xl transform translate-x-full transition-transform duration-300 z-[100] border-l border-border">
    {customizer_tw}
  </div>
"""
    
    # Inject just before <footer>
    content = content.replace('<!-- ═══════════════ FOOTER ═══════════════ -->', slide_over_container + '\n  <!-- ═══════════════ FOOTER ═══════════════ -->')

# 6. Add slide-over JS
js_functions = """
    // SLIDE OVER LOGIC
    const customizerPanel = document.getElementById('customizer-panel');
    const customizerBackdrop = document.getElementById('customizer-backdrop');

    function openCustomizer() {
      customizerPanel.classList.remove('translate-x-full');
      customizerBackdrop.classList.remove('hidden');
      // small delay for transition
      setTimeout(() => {
        customizerBackdrop.classList.remove('opacity-0');
      }, 10);
    }

    function closeCustomizer() {
      customizerPanel.classList.add('translate-x-full');
      customizerBackdrop.classList.add('opacity-0');
      setTimeout(() => {
        customizerBackdrop.classList.add('hidden');
      }, 300);
    }
"""

content = content.replace('// COMPTEURS ANIMÉS', js_functions + '\n    // COMPTEURS ANIMÉS')

with open('/Users/ayoubesqalli/Documents/GitHub/Rush/rush_homepage_v3.html', 'w') as f:
    f.write(content)

print("Migration script executed successfully.")
