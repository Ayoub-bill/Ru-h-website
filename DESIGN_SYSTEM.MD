# DESIGN SYSTEM : RU$H

## Le Manuel d'Exécution UI/UX

---

## 1. PHILOSOPHIE VISUELLE

L'interface RU$H ne doit jamais ressembler à un logiciel RH ou à un SaaS de gestion comptable. C'est un **moteur d'action**. Le design doit transpirer la vitesse, l'efficacité et l'énergie urbaine.

### Les 3 règles d'or du design RU$H :
* **Zéro décoration :** Si un élément ne sert pas à convertir ou à guider l'œil, il est supprimé.
* **Brutalisme maîtrisé :** Des lignes franches, des contrastes violents, aucune mollesse.
* **L'urgence par le vide :** L'interface respire grâce à des marges massives, ce qui rend les points d'interaction (Boutons oranges) impossibles à rater.

---

## 2. LA GRILLE ET LA STRUCTURE (BENTO SYSTEM)

Nous utilisons un système de grille stricte inspiré de l'architecture et du **"Bento Design"**.

* **Bordures (Borders) :** Lignes de séparation ultra-fines et nettes (`1px solid #000000` en mode clair, ou `#333333` en mode sombre).
* **Asymétrie :** Les blocs n'ont pas tous la même taille. On privilégie une hiérarchie visuelle forte (ex: un bloc majeur qui prend 2 colonnes, entouré de blocs mineurs).
* **Marges (Paddings) :** Généreuses et mathématiques. Les contenus ne touchent jamais les bords des boîtes. Laissez respirer la donnée.
* **Angles (Border-radius) :** Angles droits (`0px`) ou micro-arrondis (`4px` maximum) pour un aspect tranchant et industriel. Absolument aucune carte flottante ultra-arrondie.

---

## 3. PALETTE DE COULEURS (RATIO 60/30/10)

Le respect de cette répartition est fondamental. Si tout devient orange, plus rien n'est urgent.

### ⬜ 60% - La Structure et la Respiration (Fonds)
* **Blanc Pur :** `#FFFFFF` (Surface principale en mode Light)
* **Gris Industriel :** `#F5F5F7` (Fond de page en mode Light pour détacher les blocs blancs)
* **Noir Profond :** `#0A0A0A` (Fond de page en mode Dark)
* **Gris Carbone :** `#141414` (Surface principale en mode Dark)

### ⬛ 30% - La Typographie et le Contraste (Textes & Lignes)
* **Noir Mat :** `#000000` (Couleur de texte principale, lignes de structure)
* **Gris Muted :** `#666666` (Textes secondaires, descriptions)
* **Blanc Pur :** `#FFFFFF` (Texte principal en mode Dark)

### 🟧 10% - L'Impulsion (Appels à l'action)
* **Orange Vibrant (Primary) :** `#FF3D00`
* **Orange Hover (Interaction) :** `#E63600`

> [!WARNING]
> **Règle stricte :** L'orange est exclusivement réservé aux Call To Action (CTA), aux états actifs et aux points de focus monétaires (ex: prix, gains).

---

## 4. TYPOGRAPHIE

Une seule famille typographique autorisée : **Le Futura**. *(Fallback web: Jost si Futura est indisponible)*.

Le texte est traité comme un bloc architectural.

### Titres (Headers / H1, H2, H3) :
* **Police :** Futura Bold Condensed Oblique (ou italic)
* **Casse :** TOUT EN MAJUSCULES (Uppercase)
* **Traitement :** Massif, interligne très serré (`line-height: 0.9` à `1.1`), espacement des lettres négatif (`letter-spacing: -0.02em`).
* *Optionnel :* Le "cropping" (rognage partiel du texte en bordure d'écran) est autorisé pour le dynamisme.

### Interface & Corps de texte (Body / UI) :
* **Police :** Futura Medium, Book ou Regular
* **Casse :** Standard
* **Traitement :** Précis et fonctionnel. Paragraphes extrêmement courts (jamais plus de 3 lignes). Aucun crénage étiré artificiellement.

---

## 5. COMPOSANTS UI & INTERACTIFS

### Boutons
* **Bouton Primaire (Action forte) :** Fond `#FF3D00`, texte `#FFFFFF`.
* **Bouton Secondaire (Ghost) :** Fond transparent, bordure `#000000` (ou `#FFFFFF` en dark mode), texte de la couleur de la bordure.
* **Style :** Rectangulaires. Typographie toujours en Majuscules + Gras.

> [!CAUTION]
> **Interdiction absolue :** Pas d'ombres portées (`box-shadow`), pas de dégradés (`gradients`).

### Formulaires & Inputs
* Minimalistes. Une simple ligne inférieure (`border-bottom: 2px solid #000`) ou un rectangle strict sans fond.
* **Focus state :** Le contour devient Noir Mat épais ou Orange Vibrant. Pas de "glow" ou de halo flouté.

---

## 6. MOTION DESIGN & ANIMATIONS

Le mouvement chez RU$H doit évoquer la vélocité et l'impact.

* **Courbes de bézier (Easing) :** Rapides au démarrage, freinage sec à la fin (ex: `cubic-bezier(0.25, 1, 0.5, 1)`).
* **Durée :** Très court. Entre 150ms et 300ms maximum.
* **Types de transition autorisés :**
  * Slide sec (directionnel horizontal ou vertical).
  * Reveal par masque (le texte ou l'image apparaît d'un bloc net).
  * Changement de couleur instantané ou très rapide au hover.

> [!CAUTION]
> **Interdictions absolues :** Effets élastiques (bounce), animations molles, fondus au noir trop lents (fade-in langoureux), effets 3D ou parallaxes gadgets.

---

## 7. PHOTOGRAPHIE ET ICONOGRAPHIE

### La Photographie
Fini les banques d'images d'employés qui sourient devant un ordinateur. On veut la réalité du fast-food.

* **Esthétique :** Style "Paparazzi" urbain ou photographie de rue.
* **Technique :** Hard flash (flash direct), ombres portées dures derrière les sujets, hauts contrastes.
* **Sujets :** Le chaos organisé d'une cuisine, des mains qui s'échangent des plateaux, des livreurs dans la rue.
* **Effets :** Motion blur (flou de mouvement) contrôlé pour illustrer la frénésie et la vitesse de la marque.

### L'Iconographie
Si des icônes sont nécessaires, elles doivent être brutes, épaisses et géométriques.

> [!WARNING]
> Fini les illustrations "SaaS pastel", les personnages vectoriels en 3D ou les formes organiques douces.