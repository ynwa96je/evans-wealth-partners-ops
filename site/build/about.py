from ewp_lib import *
import ewp_lib, json
ewp_lib.PAGE[0] = "about"

def gallery_item(img_key, caption, extra_item=(), photo_extra=(), on_navy=False, size="medium_large"):
    cap_cl = ["ewp-caption-on-navy", "ewp-caption"] if on_navy else ["ewp-caption"]
    return box([*extra_item, "ewp-gallery-item"], [
        image(img_key, size, *photo_extra, "ewp-photo-gallery"),
        para(caption, *cap_cl),
    ])

def milestone(place, text, note=None):
    body = [para(place, "ewp-milestone-place", tag="span"), para(text, "ewp-milestone-text", tag="span")]
    if note:
        body.append(para(note, "ewp-milestone-note", tag="span"))
    return box(["ewp-milestone"], [svg("ewp-milestone-ring.svg", "ewp-milestone-marker"), box(["ewp-milestone-body"], body)])

# 1. Intro
intro_sec = section(["ewp-section-intro", "ewp-section"], [
    box(["ewp-intro"], [
        box(["ewp-intro-copy"], [
            para("About us", "ewp-eyebrow"),
            heading("A family firm, started by someone who has been the owner.", "h1", "ewp-title-page"),
            para('Evans Wealth Partners is run by John "Jack" Evans and his family from Avon, Connecticut. We built it the way we would want our own family\'s money looked after: plan first, plain English, and the same faces every year.', "ewp-text-lead"),
            box(["ewp-action-row"], [button("Book an intro call", "/contact/", "ewp-button-primary", "ewp-button")]),
        ]),
        box(["ewp-intro-media"], [image("about-intro", "large", "ewp-photo-intro")]),
    ]),
], "intro")

# 2. John's story
story_sec = section(["ewp-section-raised", "ewp-section"], [
    box(["ewp-story"], [
        box(["ewp-story-copy"], [
            para("John's story", "ewp-eyebrow"),
            heading("From behind the bar to beside the client.", "h2", "ewp-title-section"),
            para("I grew up in England and took on my first pub at 21. At the time that made me the youngest publican in England. Running a pub teaches you cash flow fast, because the bills arrive whether the regulars do or not.", "ewp-text-body"),
            para('After that I founded Xtra Time, a youth soccer coaching business in Cardiff, for which I received an Entrepreneurial award from the Welsh Assembly, and later worked as a regional sales director with Major League Soccer. Here in Connecticut I owned The Zoo Health Club in Simsbury and received an official citation from the General Assembly in recognition of becoming a citizen and owning and operating a business in the true "American dream" fashion.', "ewp-text-body"),
            para("For more than seven years I have worked as a financial advisor at a bank, a broker-dealer and an insurance-affiliated firm. I started Evans Wealth Partners so that every client gets a plan first, and every recommendation can be traced back to it.", "ewp-text-body"),
            para("Most people call me Jack. You'll speak to me on your first call.", "ewp-text-body"),
        ]),
        box(["ewp-milestone-list"], [
            milestone("England", "Ran my own pub at 21"),
            milestone("Cardiff, Wales", "Founded Xtra Time youth soccer coaching", "Entrepreneurial award, Welsh Assembly"),
            milestone("United States", "Regional sales director with Major League Soccer"),
            milestone("Simsbury, Connecticut", "Owned The Zoo Health Club", "Official citation, Connecticut General Assembly"),
            milestone("Bank, broker-dealer and insurance firm", "Seven years as a financial advisor"),
            milestone("Avon, Connecticut", "Founded Evans Wealth Partners"),
        ]),
    ]),
], "story")

# 3. How we work
principles = [
    ("ewp-icon-plan-map.svg", "The plan comes first", "We don't recommend a product until there is a written plan that shows why you need it."),
    ("ewp-icon-plain-english-chat.svg", "Plain English", "We explain every recommendation in words you would use yourself, and put the key numbers on one page."),
    ("ewp-icon-costs-document.svg", "Costs in writing", "Before you commit to anything, you get our fees in writing, in dollars as well as percentages."),
    ("ewp-icon-phone.svg", "We pick up the phone", "A new baby, a job offer, an offer for your business. Call us and we'll look at the plan together."),
]
how_sec = section(["ewp-section"], [
    box(["ewp-section-head"], [
        para("How we work", "ewp-eyebrow"),
        heading("Four things every client can expect from us.", "h2", "ewp-title-section"),
    ]),
    box(["ewp-card-list"], [box(["ewp-card-principle", "ewp-card-service"], [
        box(["ewp-icon-box"], [svg(ic, "ewp-icon")]),
        heading(t, "h3", "ewp-title-card"),
        para(b, "ewp-text-body"),
    ], tag="article") for ic, t, b in principles]),
], "how")

# 4. Family first
family_sec = section(["ewp-section-raised", "ewp-section"], [
    box(["ewp-section-head"], [
        para("Family first", "ewp-eyebrow"),
        heading("Our name is on the door.", "h2", "ewp-title-section"),
        para("We're a family business, and family is the reason most people come to see us. These are the people and places that matter to us.", "ewp-text-lead"),
    ]),
    box(["ewp-gallery"], [
        gallery_item("family", "Christmas with the family"),
        gallery_item("about-kickabout", "Never too young for a kickabout"),
        gallery_item("about-anfield", "Anfield, Liverpool"),
    ]),
    box(["ewp-gallery"], [
        gallery_item("about-liverpool-fan", "A Liverpool fan from the start"),
        gallery_item("about-evans-arms", "The Evans family arms"),
        gallery_item("about-golf", "Off the clock"),
    ]),
], "family")

# 5. In the community
community_sec = section(["ewp-section-navy", "ewp-section"], [
    box(["ewp-section-head"], [
        para("In the community", "ewp-eyebrow-on-navy", "ewp-eyebrow"),
        heading("On the touchline most weekends.", "h2", "ewp-title-on-navy", "ewp-title-section"),
        para("Soccer has been part of John's working life since Cardiff, and it still fills his weekends. Since 2024 he has coached the Hartford Athletic Youth Academy U17 boys. Before that, from 2016 to 2024, he coached Avon Travel Soccer, his daughter's team.", "ewp-text-on-navy", "ewp-text-lead"),
    ]),
    box(["ewp-gallery"], [
        box(["ewp-gallery-item"], [
            box(["ewp-badge-tile"], [image("about-hartford-crest", "medium", "ewp-photo-badge")]),
            para("Hartford Athletic Youth Academy, U17 boys coach since 2024", "ewp-caption-on-navy", "ewp-caption"),
        ]),
        gallery_item("about-coaching-staff", "With the Hartford Athletic coaching staff", extra_item=["ewp-gallery-wide"], on_navy=True, size="large"),
    ]),
    box(["ewp-gallery"], [
        gallery_item("about-anthem", "John's daughter singing the national anthem before Hartford Athletic's cup semi-final in 2026", photo_extra=["ewp-photo-top"], on_navy=True),
        gallery_item("about-avon-travel", "Avon Travel Soccer, coached by John from 2016 to 2024", on_navy=True),
        gallery_item("about-avon-travel-summer", "Avon Travel Soccer, summer season", on_navy=True),
    ]),
], "community")

# 6. Booking band
booking_sec = section(["ewp-section-booking", "ewp-section"], [
    box(["ewp-booking"], [
        box(["ewp-booking-copy"], [
            heading("Talk to John directly.", "h2", "ewp-title-section"),
            para("The first call is 30 minutes and there is no charge for it. If we're not the right fit, we'll say so.", "ewp-text-body"),
        ]),
        button("Book an intro call", "/contact/", "ewp-button-primary", "ewp-button"),
    ]),
], "booking")

page = {"title": "About", "slug": "about",
        "titles": ["Intro", "John's story", "How we work", "Family first", "In the community", "Booking band"],
        "elements": [intro_sec, story_sec, how_sec, family_sec, community_sec, booking_sec]}

defined = {c["label"] for c in CLASSES}
used = set()
def walk(e):
    used.update(e["settings"].get("classes", {}).get("value", []))
    for c in e["elements"]:
        walk(c)
for e in page["elements"]:
    walk(e)
assert used <= defined, used - defined
imgs = set()
def walk_img(o):
    if isinstance(o, dict):
        for v in o.values(): walk_img(v)
    elif isinstance(o, list):
        for v in o: walk_img(v)
    elif isinstance(o, str) and o.startswith("__ATT__"):
        imgs.add(o[7:])
walk_img(page)
print("about: classes used", len(used), "| attachments referenced:", sorted(imgs))
json.dump({"classes": CLASSES, "page": page}, open("about_build.json", "w"))
