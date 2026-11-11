from ewp_lib import *
import ewp_lib, json
ewp_lib.PAGE[0] = "home"

# 1. Banner
banner = box(["ewp-banner"], [
    image("banner", "full", "ewp-banner-photo"),
    box(["ewp-banner-scrim"], [
        box(["ewp-banner-inner"], [
            para("Wealth management in Avon, the Farmington Valley, Connecticut and beyond", "ewp-eyebrow-on-navy", "ewp-eyebrow"),
            heading("Live the life you want.", "h1", "ewp-banner-title"),
            para("Evans Wealth Partners is a family-run firm for families and business owners. We write your financial plan first, then set up your investments, insurance, retirement income and estate to match it.", "ewp-banner-lead"),
            box(["ewp-action-row"], [
                button("Book an intro call", "/contact/", "ewp-button-primary", "ewp-button"),
                button("See our services", "/services/", "ewp-button-on-navy", "ewp-button"),
            ]),
            para("The first call is 30 minutes, by phone or video, and there is no charge for it.", "ewp-banner-note"),
        ]),
    ]),
], tag="section")

# 2. Facts strip
facts = [
    ("The plan comes first", "Every client starts with a written plan. Products only come in when the plan calls for them."),
    ("Run by a family", "You work with the same people every year, and they know your goals without a recap."),
    ("Owners advising owners", "John has run a pub, a health club and a coaching business. He knows what a tight payroll week feels like."),
    ("Serving Avon, the Farmington Valley, Connecticut and beyond.", "We can meet at your business, your kitchen table or on a virtual call."),
]
facts_sec = section(["ewp-section-tight", "ewp-section-raised", "ewp-section"], [
    box(["ewp-fact-list"], [box(["ewp-fact"], [para(t, "ewp-fact-title"), para(b, "ewp-text-body")]) for t, b in facts])
], "facts")

# 3. Who we work with
who_sec = section(["ewp-section"], [
    box(["ewp-section-head"], [
        para("Who we work with", "ewp-eyebrow"),
        heading("Families and business owners, often in the same household.", "h2", "ewp-title-section"),
    ]),
    box(["ewp-card-list"], [
        box(["ewp-card-audience"], [
            image("family", "large", "ewp-photo-card"),
            heading("Families", "h3", "ewp-title-card"),
            para("Parents saving for college and retirement at the same time. Couples five to ten years from retiring. Grandparents who want to help the next generation without running short themselves.", "ewp-text-body"),
            bullets(["College and retirement saving, side by side",
                     "A retirement date you can count on, in real dollars",
                     "Wills, guardians and beneficiaries kept up to date"]),
            link_arrow("Planning for families", "/services/#planning"),
        ], tag="article"),
        box(["ewp-card-navy"], [
            para("Owner to owner", "ewp-eyebrow-on-navy", "ewp-eyebrow"),
            heading("Business owners", "h3", "ewp-title-on-navy", "ewp-title-card"),
            para("Your business is probably your biggest asset and your biggest risk. We plan the business and the household together, so a decision in one doesn't hurt the other.", "ewp-text-on-navy", "ewp-text-body"),
            bullets(["How to pay yourself, worked out with your CPA",
                     "Retirement plans for you and your team",
                     "Buy-sell funding and key person cover",
                     "A plan for selling or handing over the business"], on_navy=True),
            link_arrow("Planning for business owners", "/services/#business-planning", on_navy=True),
            box(["ewp-card-illustration"], [svg("ewp-illustration-main-street.svg", "ewp-illustration")]),
        ], tag="article"),
    ]),
    box(["ewp-callout"], [
        para("Moved here from the UK? So did John. We know the questions that come with a life split between two countries, from old pensions to bank accounts back home.", "ewp-callout-text", "ewp-text-body"),
        link_arrow("Read our UK to US guide", "/resources/"),
    ]),
], "who")

# 4. Services
services = [
    ("ewp-icon-plan-map.svg", "Financial planning", "A written plan covering cash flow, goals, taxes and your business. We update it every year and whenever life changes.", "/services/#planning"),
    ("ewp-icon-retirement-sunset.svg", "Retirement planning", "When you can stop working, what you can safely spend, and when to claim Social Security.", "/services/#retirement"),
    ("ewp-icon-investments-pie.svg", "Investments", "Portfolios built for your timeline and your tax situation, rebalanced and reported on regularly.", "/services/#investments"),
    ("ewp-icon-protection-shield.svg", "Protection strategies", "Life, disability and long-term care cover sized to what your family and your business would actually need.", "/services/#protection"),
    ("ewp-icon-income-banknote.svg", "Income strategies", "Turning your savings into a steady monthly paycheck, drawn from the right accounts in the right order.", "/services/#income"),
    ("ewp-icon-estate-house.svg", "Estate planning", "Beneficiaries, trusts and business succession, coordinated with your attorney so nothing falls through the gaps.", "/services/#estate"),
]
service_cards = [box(["ewp-card-service"], [
    box(["ewp-icon-box"], [svg(ic, "ewp-icon")]),
    heading(t, "h3", "ewp-title-card"),
    para(b, "ewp-text-body"),
    link_arrow("Learn more", href),
], tag="article") for ic, t, b, href in services]
service_cards.append(box(["ewp-card-feature", "ewp-card-service"], [
    box(["ewp-icon-box-on-navy", "ewp-icon-box"], [svg("ewp-icon-business-briefcase.svg", "ewp-icon")]),
    heading("Business planning", "h3", "ewp-title-on-navy", "ewp-title-card"),
    para("Employee plans and benefits, cash and risk management, business structure, buy-sell agreements, key person cover, and a plan for the day you sell or hand over.", "ewp-text-on-navy", "ewp-text-body"),
    link_arrow("Learn more", "/services/#business-planning", on_navy=True),
], tag="article"))
services_sec = section(["ewp-section-raised", "ewp-section"], [
    box(["ewp-section-head"], [
        para("Services", "ewp-eyebrow"),
        heading("One plan, seven areas of advice.", "h2", "ewp-title-section"),
        para("Each service ties back to your plan, so a choice about insurance or investments never works against your retirement or your estate.", "ewp-text-lead"),
    ]),
    box(["ewp-card-list"], service_cards),
], "services")

# 5. How it works
steps = [
    ("01", "Intro call", "Thirty minutes. You tell us what's on your mind, and we tell you honestly whether we're a good fit."),
    ("02", "Discovery meeting", "We gather the numbers: accounts, tax returns, policies and business financials. We also ask what you want the next ten years to look like."),
    ("03", "Your written plan", "We walk you through clear recommendations, what each one costs and the order to do them in."),
    ("04", "Ongoing advice", "We review the plan with you at least once a year. When something changes, you call and we adjust."),
]
how_sec = section(["ewp-section-navy", "ewp-section"], [
    box(["ewp-section-head"], [
        para("How it works", "ewp-eyebrow-on-navy", "ewp-eyebrow"),
        heading("From first call to a plan you can use.", "h2", "ewp-title-on-navy", "ewp-title-section"),
    ]),
    box(["ewp-step-list"], [box(["ewp-step"], [
        para(n, "ewp-step-number", tag="span"),
        heading(t, "h3", "ewp-title-on-navy", "ewp-title-card"),
        para(b, "ewp-text-on-navy", "ewp-text-body"),
    ]) for n, t, b in steps]),
    box(["ewp-action-row"], [button("Book an intro call", "/contact/", "ewp-button-primary", "ewp-button")]),
], "how")

# 6. Meet the founder
founder_sec = section(["ewp-section"], [
    box(["ewp-feature"], [
        image("portrait", "medium_large", "ewp-photo-portrait"),
        box(["ewp-feature-copy"], [
            para("Meet the founder", "ewp-eyebrow"),
            heading('John "Jack" Evans', "h2", "ewp-title-section"),
            para("John grew up in England and was running his own pub at 21, the youngest publican in England. He went on to found a youth soccer coaching business in Cardiff, serve as a regional sales director with Major League Soccer, and own The Zoo Health Club in Simsbury.", "ewp-text-body"),
            para("He has spent more than seven years advising families at a bank, a broker-dealer and an insurance-affiliated firm. Evans Wealth Partners is where he puts all of it together.", "ewp-text-body"),
            link_arrow("Read John's story", "/about/"),
        ]),
    ]),
], "founder")

# 7. Based in Avon
avon_sec = section(["ewp-section-raised", "ewp-section"], [
    box(["ewp-split"], [
        box(["ewp-split-media"], [image("river", "large", "ewp-photo-band")]),
        box(["ewp-split-copy"], [
            para("Based in Avon", "ewp-eyebrow"),
            heading("Rooted in Avon. Working across Connecticut and beyond.", "h2", "ewp-title-section"),
            para("We live, work and coach youth soccer here in the Farmington Valley. Our clients are families and businesses in Avon, the Farmington Valley, Connecticut and beyond, not just those down the road.", "ewp-text-body"),
            para("Most of our meetings happen virtually, so where you are is never a barrier. When you'd rather meet in person, we'll come to your home or your business.", "ewp-text-body"),
            link_arrow("Ways to meet", "/contact/"),
        ]),
    ]),
], "avon")

# 8. Booking band
booking_sec = section(["ewp-section-booking", "ewp-section"], [
    box(["ewp-booking"], [
        box(["ewp-booking-copy"], [
            heading("Start with a 30-minute call.", "h2", "ewp-title-section"),
            para("Bring your questions. We'll tell you what we would look at first, and whether we're the right firm for you.", "ewp-text-body"),
        ]),
        button("Book an intro call", "/contact/", "ewp-button-primary", "ewp-button"),
    ]),
], "booking")

# 7b. FAQ (approved copy, see ewp_lib.FAQ)
faq_sec = faq_section([FAQ[k] for k in ["based", "avon", "what", "owners"]], ["ewp-section"])

page = {"title": "Home", "slug": "home",
        "titles": ["Banner", "Facts", "Who we work with", "Services", "How we work", "Founder", "Avon", "FAQ", "Booking band"],
        "elements": [banner, facts_sec, who_sec, services_sec, how_sec, founder_sec, avon_sec, faq_sec, booking_sec]}

# sanity: every class used is defined, and every defined class is used
defined = {c["label"] for c in CLASSES}
used = set()
def walk(e):
    for l in e["settings"].get("classes", {}).get("value", []):
        used.add(l)
    for c in e["elements"]:
        walk(c)
for e in page["elements"]:
    walk(e)
assert used <= defined, used - defined
print("classes defined:", len(defined), "unused:", sorted(defined - used))
json.dump({"classes": CLASSES, "page": page}, open("home_build.json", "w"))
print("written")

