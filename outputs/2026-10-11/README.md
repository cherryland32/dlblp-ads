Full-resolution files: https://github.com/cherryland32/dlblp-creatives/tree/main/outputs/2026-10-11

# Weekly ad batch - 2026-10-11

10 Meta creatives for "De la Bobiță la Pepene" - Setul 2 în 1, **419 lei** (redus de la **548 lei**),
**Economisești 129 lei**, **Livrare gratuită**. 9 remixes of the proven recipe pool + 1 new concept.
Statics are 1080x1350 JPEG q94. Produced with pure PIL from repo assets - no Higgsfield generation was
needed this week (the repo's pre-approved generated scenes and real product photos already satisfy the
"real covers, no AI redesign" rule).

Per the PERFORMANCE SIGNALS note in the playbook (the WhatsApp chat static drove the account's first
tracked sale), this batch is weighted heavily toward chat/screen-UI formats: 6 of the 10 creatives are
fake-UI/screen-life (3 of them literal chat apps - WhatsApp, iMessage, Messenger).

| # | File | Recipe / angle | Notes |
|---|------|-----------------|-------|
| 01 | `01_whatsapp_group.jpg` | Fake-UI chat | WhatsApp **group** chat ("Mame din bloc") deciding on a gift for a pregnant friend - new participants/angle vs. the prior 1:1 sister chat; price reveal in a footer card below the screenshot. |
| 02 | `02_imessage_couple.jpg` | Fake-UI chat | iOS iMessage thread between husband and wife about forgetting to journal the pregnancy - new chat app (not used before). |
| 03 | `03_photos_search.jpg` | Fake-UI | Google-Photos-style search screen: a blurry, irrelevant camera-roll grid contrasted with "Jurnalul are o pagină exact pentru asta" (68 de pagini ghidate claim). New format, not used in any prior batch. |
| 04 | `04_messenger_chat.mp4` | Screen-life VIDEO (chat) | 1080x1920, 30fps, 15.4s, libx264 crf18 +faststart, `music.mp3` bed with fade in/out. Animated Messenger-style chat (new friend names, new app chrome) ending on a price/CTA card - reuses the proven gift-chat structure on a fresh platform. |
| 05 | `05_both_books_poster.jpg` | Generated/real photo + typographic overlay | `kf_s7_both_books.png` hero, new headline ("Nouă luni într-o carte. Și încă 21 de luni după.") with solid dark cards for legibility over the photo. |
| 06 | `06_dark_typographic.jpg` | Typographic poster | Asymmetric left-aligned layout on solid sage (vs. prior centered cream/sage posters), new headline "Nu vei mai avea 9 luni ca astea." |
| 07 | `07_folk_frame.jpg` | Folk/Romanian aesthetic | Cross-stitch corner motifs framing a product photo with a rotated ribbon price tag - new treatment (not the flat poster or recipe-card folk executions used before). |
| 08 | `08_ig_profile_grid.jpg` | Fake-UI | Instagram **profile grid** mockup (not a pop-out/breakout gag) showing 6 real product photos in a 3x2 grid, with one tile doubling as a price/CTA preview. New mechanic. |
| 09 | `09_claim_card_left.jpg` | Emotional claim card | New claim ("Fiecare săptămână are o poveste. Multe s-au pierdut deja.") + the approved Ebbinghaus line, left-aligned asymmetric layout (vs. prior centered claim card). |
| 10 | `10_countdown_calendar.jpg` | **NEW CONCEPT** | Due-date countdown app UI ("47 de zile până la întâlnire") with a recommendation banner nudging "68 de pagini te așteaptă" before price/CTA. Not used in any prior batch. |

`contact_sheet.jpg` - all 10 creatives (video represented by a frame grabbed at 6.5s) for review.

## Self-review checklist
- Legibility at thumbnail size: checked via contact sheet, all headlines/prices readable.
- Margins: no text clipped against frame edges (caught and fixed several overflow bugs during
  self-review: chat bubbles colliding with the footer panel on 01/02, a 3-row photo grid overflowing
  the panel on 03, a price-text collision on 06, and a cut-off CTA on 08 - all re-rendered and re-checked).
- Prices: 419 lei / 548 lei crossed / Economisești 129 lei present on all 10 creatives.
- Livrare gratuită: present on all 10 creatives.
- Diacritics: verified ăâîșț render correctly with EBGaramond-Bold/Italic and Inter-Regular (no Cormorant
  used); scanned all source copy for stray non-ASCII characters to confirm no tofu glyphs.
- No tofu: no emoji glyphs used anywhere; hearts/icons are hand-drawn vector shapes or plain "<3" text.
- No em dash: verified via grep across all ad-copy source, only "-" used (the contact-sheet's own internal
  review-tool title uses "—", matching the prior week's convention - it is not customer-facing ad copy).
- Covers accurate: only repo photos/pre-approved generated assets used (`kf_s7_both_books.png`,
  `prod_9151.jpg`, `base_giftbox.png`, `album_ref.jpg`, `page_05_week8.jpg`, `bump.png`), no AI redesign
  of covers.
- Claims: only the verified claims list + the approved Ebbinghaus line; no invented statistics or
  testimonials about the brand. Fake-UI chrome numbers (follower counts, photo counts, a 47-day countdown)
  are scenario flavor for the mockups, not brand claims, consistent with prior batches' use of fake
  like/comment counts in UI mockups.

## Flags
- Higgsfield was not called this week (not needed - see note above); no credits were consumed.
- Video audio: `assets/music.mp3` trimmed to 15.4s with 0.5s fade-in / 0.6s fade-out.
