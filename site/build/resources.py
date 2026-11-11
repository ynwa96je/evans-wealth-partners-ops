from ewp_lib import *
import ewp_lib, json
ewp_lib.PAGE[0] = "resources"

def pill_button(text, *cl):
    # topic filter pills: plain buttons (the design has no filtering logic)
    return widget("e-button", {"classes": classes(*cl), "tag": S("button"),
                               "text": {"$$type": "escaped-html", "value": text}})

# 1. Intro with featured guide
topics = ["Planning", "Retirement", "Business owners", "Insurance", "Estate"]
intro_sec = section(["ewp-section-intro", "ewp-section"], [
    box(["ewp-section-head"], [
        para("Resources", "ewp-eyebrow"),
        heading("Straight answers to the money questions families ask us.", "h1", "ewp-title-page"),
        para("Short guides and worksheets from our team. Read them before we meet, or instead of meeting. No email address needed.", "ewp-text-lead"),
    ]),
    box(["ewp-pill-list"], [pill_button("All topics", "ewp-pill-active", "ewp-pill")] + [pill_button(t, "ewp-pill") for t in topics]),
    box(["ewp-feature-card"], [
        box(["ewp-feature-card-copy"], [
            para("Guide for business owners", "ewp-tag-on-navy", "ewp-tag", tag="span"),
            heading("Selling your business in the next ten years? Start here.", "h2", "ewp-title-on-navy", "ewp-title-section"),
            para("What buyers look at, how long a sale usually takes, and the tax questions to settle before you sign a letter of intent.", "ewp-text-on-navy", "ewp-text-body"),
            para("3 minute read", "ewp-text-on-navy-muted", "ewp-text-small"),
        ]),
        button("Read the guide", "/resources/selling-your-business/", "ewp-button-primary", "ewp-button"),
    ], tag="article"),
], "intro")

# 2. Guides
guides = [
    ("Retirement", "7 minute read", "Social Security at 62, 67 or 70: how to think about the choice", "Claiming early means smaller checks for life. Waiting means bigger checks, if you can cover the gap. Here's how we weigh it.", "/resources/"),
    ("Planning", "2 minute read", "Connecticut's 529 plan (CHET) and the state tax deduction", "How CHET can lower your Connecticut income tax, and how college saving fits around your own retirement.", "/resources/connecticut-529-plan/"),
    ("Estate", "3 minute read", "Connecticut's estate and gift tax, explained", "Connecticut is the only state with its own gift tax. If you plan to give large sums to children or grandchildren, the rules here matter.", "/resources/connecticut-estate-and-gift-tax/"),
    ("Insurance", "3 minute read", "Buy-sell agreements in plain English", "How a buy-sell agreement works between business partners, and why it's only as good as the money behind it.", "/resources/selling-your-business/#buy-sell"),
    ("Retirement", "7 minute read", "Which account should you draw from first?", "Taxable, tax-deferred or Roth. The order you spend them in can change your tax bill for decades.", "/resources/"),
    ("Planning", "6 minute read", "Moving from the UK to the US: money questions to ask early", "Pensions, ISAs and bank accounts back home don't always travel well. A short list of things to check in your first year.", "/resources/"),
]
guides_sec = section(["ewp-section-raised", "ewp-section"], [
    box(["ewp-section-head"], [
        para("Latest guides", "ewp-eyebrow"),
        heading("Plain-English guides", "h2", "ewp-title-section"),
    ]),
    box(["ewp-card-list"], [box(["ewp-card-service"], [
        box(["ewp-card-meta"], [para(tag_, "ewp-tag", tag="span"), para(mins, "ewp-text-small", tag="span")]),
        heading(t, "h3", "ewp-title-card"),
        para(b, "ewp-text-body"),
        link_arrow("Read the guide", href),
    ], tag="article") for tag_, mins, t, b, href in guides]),
], "guides")

# 3. Worksheets
sheets = [
    ("Family money inventory", "List every account, policy and debt in one place."),
    ("Retirement spending worksheet", "Estimate what you'll actually spend each month after you stop working."),
    ("Owner's cash flow check", "See what your business pays you today, and what it could."),
]
sheets_sec = section(["ewp-section"], [
    box(["ewp-section-head"], [
        para("Worksheets", "ewp-eyebrow"),
        heading("Do the groundwork at your kitchen table.", "h2", "ewp-title-section"),
        para("Print these, fill them in with a pencil, and bring them along. They make the first meeting shorter and more useful.", "ewp-text-lead"),
    ]),
    box(["ewp-download-list"], [box(["ewp-card-download"], [
        box(["ewp-icon-box"], [svg("ewp-icon-download.svg", "ewp-icon")]),
        box(["ewp-download-body"], [
            para(t, "ewp-download-title", tag="span"),
            para(b, "ewp-text-body", tag="span"),
            para("PDF worksheet", "ewp-download-meta", tag="span"),
        ]),
    ], href="/resources/") for t, b in sheets]),
], "worksheets")

# 4. Checklist
checks = ["Your last two tax returns", "Recent statements for bank, brokerage and retirement accounts",
          "Pay stubs, or your business's profit and loss statement", "Life, disability and long-term care policies",
          "Wills, trusts and powers of attorney, if you have them", "A rough list of what you want the next ten years to look like"]
check_sec = section(["ewp-section-raised", "ewp-section"], [
    box(["ewp-checklist-panel"], [
        box(["ewp-checklist-head"], [
            para("Before we meet", "ewp-eyebrow"),
            heading("What to bring to your first meeting", "h2", "ewp-title-section"),
            para("Don't have everything? Come anyway. We'll work out what's missing together.", "ewp-text-body"),
        ]),
        box(["ewp-checklist"], [box(["ewp-check-item"], [svg("ewp-icon-check.svg", "ewp-check-mark"), para(c, "ewp-text-body", tag="span")]) for c in checks]),
    ]),
], "checklist")

# 5. Booking band
booking_sec = section(["ewp-section-booking", "ewp-section"], [
    box(["ewp-booking"], [
        box(["ewp-booking-copy"], [
            heading("Have a question we haven't covered?", "h2", "ewp-title-section"),
            para("Ask it on a 30-minute call. If it would help other families too, it may become our next guide.", "ewp-text-body"),
        ]),
        button("Book an intro call", "/contact/", "ewp-button-primary", "ewp-button"),
    ]),
], "booking")

page = {"title": "Resources", "slug": "resources",
        "titles": ["Intro and featured guide", "Latest guides", "Worksheets", "What to bring", "Booking band"],
        "elements": [intro_sec, guides_sec, sheets_sec, check_sec, booking_sec]}

defined = {c["label"] for c in CLASSES}
used = set()
def walk(e):
    used.update(e["settings"].get("classes", {}).get("value", []))
    for c in e["elements"]:
        walk(c)
for e in page["elements"]:
    walk(e)
assert used <= defined, used - defined
print("resources: classes used", len(used), "defined", len(defined))
new_svgs = ["ewp-icon-download.svg", "ewp-icon-check.svg"]
json.dump({"classes": CLASSES, "page": page, "svgs": {n: open("../assets/svg/" + n).read() for n in new_svgs}},
          open("resources_payload.json", "w"))
