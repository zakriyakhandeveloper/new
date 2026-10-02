# -*- coding: utf-8 -*-
"""NameVerse curated identity table for batch 1 (islamic: aamilah..aaus).

Every row records what could actually be established for the form, with an
explicit confidence level. Rows whose form could not be matched to any
Tier-1/Tier-2 lexical source are marked UNKNOWN and their meaning field carries
an explicit 'not established' statement instead of an invented gloss.

Format (pipe-separated, one row per name):
  slug | origin | short_meaning | arabic_script | root_analysis | transliteration
       | confidence | gender | note
"""

RAW = """
aamilah|Arabic|Female worker; doer; one who acts|عاملة|ʿ-m-l — ʿāmila, feminine active participle of ʿamila 'to work, to do'|ʿĀmila|HIGH|Female|
aamin|Arabic|Trustworthy; faithful; reliable (also the liturgical 'amen')|آمين|ʾ-m-n — āmīn, from amina 'to be safe, to trust'|Āmīn|HIGH|Male|
aamina|Arabic|Safe; secure; trustworthy|آمنة|ʾ-m-n — āmina, feminine of āmīn|Āmina|HIGH|Female|Borne by Āmina bint Wahb, mother of the Prophet Muhammad — a documented historical bearer.
aaminaat||Not objectively established as a given name|—|—|—|UNKNOWN|Female|Not an established given name; appears to be a plural or a directory coinage. No Tier-1 confirmation found.
aaminah|Arabic|Safe; secure; trustworthy|آمنة|ʾ-m-n — variant spelling of Āmina|Āminah|HIGH|Female|
aamir|Arabic|Inhabiting; populous; flourishing; prosperous|عامر|ʿ-m-r — ʿāmir, active participle of ʿamara 'to inhabit, to build up, to flourish'|ʿĀmir|HIGH|Male|
aamira|Arabic|Inhabiting; flourishing (feminine)|عامرة|ʿ-m-r — feminine of ʿāmir|ʿĀmira|HIGH|Female|
aamirah|Arabic|Inhabiting; flourishing (feminine)|عامرة|ʿ-m-r — variant transliteration of ʿāmira|ʿĀmirah|HIGH|Female|
aamirat||Not objectively established as a given name|—|—|—|UNKNOWN|Female|Not an established given name; no Tier-1 confirmation found.
aamirul||Not objectively established as a given name|—|—|—|UNKNOWN|Male|Not an established given name; possibly a compound coinage. No evidence located.
aamiya||Not objectively established|—|—|—|UNKNOWN|Female|Not established. No Arabic lexeme matching this form could be confirmed.
aamla||Not objectively established|—|—|—|LOW|Female|The source gloss 'nourishing, supporting' is unsupported. The form coincides with Hindi/Sanskrit āmlā 'Indian gooseberry' (āmalakī), which is not an Arabic name element.
aamna|Arabic|Safe; secure; trustworthy|آمنة|ʾ-m-n — South Asian spelling of Āmina|Āmna|HIGH|Female|Variant of Āmina.
aamra|Arabic|Populous; flourishing (feminine)|عامرة|ʿ-m-r — variant of ʿāmira|ʿĀmra|MEDIUM|Female|
aamrah|Arabic|Populous; flourishing (feminine)|عامرة|ʿ-m-r — variant of ʿāmira|ʿĀmrah|MEDIUM|Female|
aana||Not objectively established|—|—|—|UNKNOWN|Female|Not established as an Arabic name; no lexeme confirmed.
aanal||Not objectively established|—|—|—|UNKNOWN|Female|Not established; no evidence located.
aanan||Not objectively established|—|—|—|UNKNOWN|Male|Not established; no evidence located.
aaneseh||Not objectively established|—|—|—|LOW|Unisex|Form suggests a Persianate construction; origin not confirmed by any Tier-1 source.
aani||Not objectively established|—|—|—|UNKNOWN|Female|Not established; no evidence located.
aania||Not objectively established|—|—|—|UNKNOWN|Female|Not established; no evidence located.
aanil||Not objectively established|—|—|—|UNKNOWN|Male|Not established; no evidence located.
aanisa|Arabic|Sociable; affable; friendly (feminine)|آنسة|ʾ-n-s — ānisa, feminine of ānis 'sociable, comforting'|Ānisa|MEDIUM|Female|
aanisah|Arabic|Sociable; affable; friendly (feminine)|آنسة|ʾ-n-s — variant transliteration of ānisa|Ānisah|MEDIUM|Female|
aaniya||Not objectively established|—|—|—|UNKNOWN|Female|Not established; no evidence located.
aaniyah||Not objectively established|—|—|—|UNKNOWN|Female|Not established; no evidence located.
aaolin||Not objectively established|—|—|—|UNKNOWN|Unisex|Form is not Arabic; no origin confirmed.
aaqib|Arabic|Follower; successor; the one who comes after|عاقب|ʿ-q-b — ʿāqib, from ʿaqaba 'to follow, to come after'|ʿĀqib|HIGH|Male|Al-ʿAqīb is named among the Prophet's titles in the Hadith of the Five Names (Bukhārī and Muslim). The exact form is not a Qur'anic word; the root ʿ-q-b occurs in the Qur'an.
aaqiba|Arabic|Consequence; successor (feminine)|عاقبة|ʿ-q-b — ʿāqiba, feminine of ʿāqib; also 'outcome, consequence'|ʿĀqiba|MEDIUM|Female|
aaqibah|Arabic|Consequence; successor (feminine)|عاقبة|ʿ-q-b — variant transliteration of ʿāqiba|ʿĀqibah|MEDIUM|Female|
aaqif|Arabic|One who stays in devotion; devoted|عاكف|ʿ-k-f — ʿākif, from ʿakafa 'to stay, to devote oneself'|ʿĀkif|MEDIUM|Male|
aaqifa|Arabic|One who stays in devotion (feminine)|عاكفة|ʿ-k-f — feminine of ʿākif|ʿĀkifa|MEDIUM|Female|
aaqil|Arabic|Intelligent; wise; prudent; one who restrains himself|عاقل|ʿ-q-l — ʿāqil, from ʿaqala 'to bind, to understand'|ʿĀqil|HIGH|Male|
aaqilah|Arabic|Intelligent; wise (feminine)|عاقلة|ʿ-q-l — feminine of ʿāqil|ʿĀqila|HIGH|Female|
aara||Not objectively established|—|—|—|LOW|Unisex|Multiple incompatible candidates (Persian ārā 'adorner'; Arabic ārāʾ 'opinions'). Origin not resolved.
aaraf|Arabic|The heights; the elevated places|أعراف|ʿ-r-f — aʿrāf, plural; title of Sūrat al-Aʿrāf (Qur'an 7)|Aʿrāf|MEDIUM|Male|The source gloss 'gardens of paradise' is unsupported: aʿrāf denotes the elevated places.
aarasun||Not objectively established|—|—|—|UNKNOWN|Unisex|Not established; no evidence located.
aareeha||Not objectively established|—|—|—|UNKNOWN|Female|Not established; no evidence located.
aarefa|Arabic|Knowing; knowledgeable (feminine)|عارفة|ʿ-r-f — ʿārifa, feminine of ʿārif|ʿĀrifa|HIGH|Female|
aarfa|Arabic|Knowing; knowledgeable (feminine)|عارفة|ʿ-r-f — variant of ʿārifa|ʿĀrfa|HIGH|Female|
aarib|Arabic|Acute; quick-witted; sensible|أريب|ʾ-r-b — arīb|Arīb|MEDIUM|Male|
aaribah|Arabic|Acute; quick-witted (feminine)|أريبة|ʾ-r-b — feminine of arīb|Arība|MEDIUM|Female|
aaribat||Not objectively established|—|—|—|UNKNOWN|Male|Not established; no evidence located.
aaribun||Not objectively established as a given name|—|—|—|LOW|Unisex|Appears to be a plural form, not a given name. No evidence as a personal name.
aarif|Arabic|Knowing; one who knows|عارف|ʿ-r-f — ʿārif, active participle of ʿarafa 'to know'|ʿĀrif|HIGH|Male|
aarifa|Arabic|Knowing; knowledgeable (feminine)|عارفة|ʿ-r-f — feminine of ʿārif|ʿĀrifa|HIGH|Female|
aarifah|Arabic|Knowing; knowledgeable (feminine)|عارفة|ʿ-r-f — variant of ʿārifa|ʿĀrifah|HIGH|Female|
aarifin|Arabic|Those who know (plural)|عارفين|ʿ-r-f — plural of ʿārif|ʿĀrifīn|LOW|Male|Plural form rather than a singular given name; recorded as used in the directory.
aariz|Arabic|Appearing; presenting; intervening|عارض|ʿ-r-ḍ — ʿāriḍ, active participle of ʿaraḍa 'to appear, to present'|ʿĀriḍ|MEDIUM|Male|Sources also gloss the form as 'intelligent' and 'rain-bearing cloud'; the sense is not settled.
aarizah|Arabic|Appearing; presenting (feminine)|عارضة|ʿ-r-ḍ — feminine of ʿāriḍ|ʿĀriḍa|MEDIUM|Female|
aarizun||Not objectively established|—|—|—|UNKNOWN|Male|Not established; no evidence located.
aaron|Hebrew|Hebrew origin; the traditional gloss 'mountain of strength' is folk etymology|هارون|Hebrew Aharon, of uncertain etymology; Arabic form Hārūn|Hārūn|HIGH|Male|Qur'anic prophet Hārūn, brother of Mūsā (Moses). The source record's 'Arabic origin', its 'mountain of strength' gloss and its celebrity list are unsupported and were removed.
aarya||Not objectively established|آريا|—|—|LOW|Female|Competing candidates (Sanskrit ārya 'noble'; Iranian āryā). Origin not resolved; the source asserted Arabic without support.
aaryan|Sanskrit|Noble; honourable; of noble descent|—|Sanskrit ārya 'noble, honourable'|Āryan|HIGH|Male|Sanskrit origin, not Arabic as the source asserted.
aarzam||Not objectively established|—|—|—|LOW|Male|Suggested Persian derivation (arjam 'more precious') is not confirmed.
aarzoo|Persian|Wish; desire; longing|آرزو|Persian ārzū 'wish, desire, longing'|Ārzū|HIGH|Female|Persian origin, not Arabic as the source asserted.
aarzu|Persian|Wish; desire; longing|آرزو|Persian ārzū — variant transliteration|Ārzū|HIGH|Female|Variant of Ārzū; Persian origin.
aas||Not objectively established|—|—|—|UNKNOWN|Male|Not established; no evidence located.
aasaal||Not objectively established|—|—|—|UNKNOWN|Male|Not established; no evidence located.
aasal||Not objectively established|—|—|—|LOW|Male|Ambiguous: Arabic aṣl 'origin, root' and ʿasal 'honey' are both possible, but neither is confirmed as this name's source.
aaseman|Persian|Sky; heaven; firmament|آسمان|Persian āsmān 'sky, heaven'|Āsemān|HIGH|Male|Persian origin, not Arabic as the source asserted.
aasfa||Not objectively established|—|—|—|UNKNOWN|Female|Not established; no evidence located.
aashif||Not objectively established|—|—|—|UNKNOWN|Male|Not established; no evidence located.
aashik|Arabic|Lover; one who is passionately in love|عاشق|ʿ-sh-q — ʿāshiq, active participle of ʿashiqa 'to love passionately'|ʿĀshiq|HIGH|Male|
aashiq|Arabic|Lover; one who is passionately in love|عاشق|ʿ-sh-q — variant transliteration of ʿāshiq|ʿĀshiq|HIGH|Male|Variant of ʿĀshiq.
aashir|Arabic|One who associates or consorts with others; tenth|عاشر|ʿ-sh-r — ʿāshir, active participle of ʿashara 'to associate, to mix with'|ʿĀshir|MEDIUM|Male|The source gloss 'wealthy, prosperous' is unsupported and was corrected.
aasia||Not objectively established|آسية|—|Āsiya|MEDIUM|Female|Associated in Islamic tradition with the wife of Pharaoh. The name's etymology is not established (Egyptian, Hebrew and Greek candidates). The source gloss 'living water' is unsupported.
aasif||Not objectively established|آصف|Arabic ʿāṣif 'stormy wind'; Āṣif is the traditional name of Solomon's vizier|Āṣif|MEDIUM|Male|Two homographs are conflated in the source: Āṣif (vizier of Sulaymān) and ʿāṣif ('tempest'). The source gloss 'helper, supporter' is unsupported.
aasifah|Arabic|Storm; tempest|عاصفة|ʿ-ṣ-f — ʿāṣifa, feminine participle of ʿaṣafa 'to blow violently'|ʿĀṣifa|MEDIUM|Female|
aasim|Arabic|Protector; defender; one who guards|عاصم|ʿ-ṣ-m — ʿāṣim, active participle of ʿaṣama 'to protect, to keep safe'|ʿĀṣim|HIGH|Male|The source gloss 'one who hastens' is unsupported and was corrected.
aasima|Arabic|Protectress; (also) capital city|عاصمة|ʿ-ṣ-m — ʿāṣima, feminine of ʿāṣim|ʿĀṣima|MEDIUM|Female|
aasimah|Arabic|Protectress|عاصمة|ʿ-ṣ-m — variant transliteration of ʿāṣima|ʿĀṣimah|MEDIUM|Female|
aasimat||Not objectively established|—|—|—|UNKNOWN|Female|Not an established given name; no evidence located.
aasir||Not objectively established|—|—|—|LOW|Male|Ambiguous (Arabic asīr 'captive'; ʿāṣir 'pressing'). Origin not resolved.
aasira||Not objectively established|—|—|—|UNKNOWN|Female|Not established; no evidence located.
aasiya||Not objectively established|آسية|—|Āsiya|MEDIUM|Female|Variant of the traditional name Āsiya; etymology not established.
aasiyah||Not objectively established|آسية|—|Āsiyah|MEDIUM|Female|Variant of Āsiya.
aasiyyah||Not objectively established|آسية|—|Āsiyyah|MEDIUM|Female|Variant of Āsiya.
aasma|Arabic|Names; (also) exalted, noble|أسماء|s-m-w — asmāʾ 'names'; the sense 'exalted' belongs to the root s-m-w|Asmāʾ|HIGH|Female|Borne by Asmāʾ bint Abī Bakr — a documented historical bearer.
aasmaa|Arabic|Names; (also) exalted, noble|أسماء|s-m-w — variant transliteration of Asmāʾ|Asmāʾ|HIGH|Female|Variant of Asmāʾ.
aasman|Persian|Sky; heaven; firmament|آسمان|Persian āsmān 'sky, heaven'|Āsmān|HIGH|Male|Persian origin, not Arabic as the source asserted.
aateqa|Arabic|Free; liberated; noble (feminine)|عاتقة|ʿ-t-q — ʿātiqa, feminine of ʿātiq|ʿĀtiqa|MEDIUM|Female|
aathira||Not objectively established|—|—|—|LOW|Female|Suggested Arabic athīra 'preferred' is not confirmed for this form.
aati||Not objectively established|—|—|—|LOW|Male|Not established; no evidence located.
aatif|Arabic|Affectionate; sympathetic; compassionate|عاطف|ʿ-ṭ-f — ʿāṭif, active participle of ʿaṭafa 'to incline, to be kind'|ʿĀṭif|HIGH|Male|The source gloss 'present, existent' is unsupported and was corrected.
aatifa|Arabic|Affection; sympathy; kindness|عاطفة|ʿ-ṭ-f — ʿāṭifa, feminine of ʿāṭif|ʿĀṭifa|HIGH|Female|
aatifah|Arabic|Affection; sympathy; kindness|عاطفة|ʿ-ṭ-f — variant transliteration of ʿāṭifa|ʿĀṭifah|HIGH|Female|
aatik|Arabic|Free; liberated; (also) of ancient vintage|عاتق|ʿ-t-q — ʿātiq; cf. ʿatīq 'ancient, freed'|ʿĀtiq|MEDIUM|Male|The source gloss 'strong, firm' is unsupported.
aatika|Arabic|Free; liberated; pure; noble (feminine)|عاتكة|ʿ-t-q — ʿātika, feminine|ʿĀtika|MEDIUM|Female|
aatikaat||Not objectively established|—|—|—|UNKNOWN|Female|Not an established given name; no evidence located.
aatikah|Arabic|Free; liberated; noble (feminine)|عاتكة|ʿ-t-q — variant transliteration of ʿātika|ʿĀtikah|MEDIUM|Female|
aatiq|Arabic|Ancient; old; freed|عتيق|ʿ-t-q — ʿatīq|ʿAtīq|MEDIUM|Male|
aatiqa|Arabic|Ancient; freed (feminine)|عتيقة|ʿ-t-q — feminine of ʿatīq|ʿAtīqa|MEDIUM|Female|
aatiqah|Arabic|Ancient; freed (feminine)|عتيقة|ʿ-t-q — variant transliteration of ʿatīqa|ʿAtīqah|MEDIUM|Female|
aatir|Arabic|Fragrant; perfumed|عاطر|ʿ-ṭ-r — ʿāṭir, from ʿiṭr 'perfume'|ʿĀṭir|HIGH|Male|
aatira|Arabic|Fragrant; perfumed (feminine)|عاطرة|ʿ-ṭ-r — feminine of ʿāṭir|ʿĀṭira|HIGH|Female|
aatirah|Arabic|Fragrant; perfumed (feminine)|عاطرة|ʿ-ṭ-r — variant transliteration of ʿāṭira|ʿĀṭirah|HIGH|Female|
aatiya||Not objectively established|—|—|—|LOW|Female|Not established; no evidence located.
aauf|Arabic|Arabic male given name and tribal name|عوف|ʿ-w-f — ʿAwf|ʿAwf|MEDIUM|Male|The source gloss 'help, support' is unsupported.
aaus|Arabic|Arabic male given name; name of the Medinan tribe al-Aws|أوس|ʾ-w-s — Aws|Aws|MEDIUM|Male|The source gloss 'fish' is unsupported and was corrected (Arabic 'fish' is ḥūt).
"""

FIELDS = ["slug", "origin", "meaning", "arabic", "root", "translit", "conf", "gender", "note"]


def load():
    out = {}
    for line in RAW.strip().split("\n"):
        if not line.strip():
            continue
        parts = line.split("|")
        parts += [""] * (len(FIELDS) - len(parts))
        row = dict(zip(FIELDS, parts[: len(FIELDS)]))
        out[row["slug"]] = row
    return out
