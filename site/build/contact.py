from ewp_lib import *
import ewp_lib, json
ewp_lib.PAGE[0] = "contact"

def contact_item(media, label, body):
    return box(["ewp-contact-item"], [media, box(["ewp-contact-item-body"], [para(label, "ewp-contact-label"), body])])

email = widget("e-paragraph", {"classes": classes("ewp-text-link", "ewp-text-body"), "tag": S("p"),
                               "paragraph": {"$$type": "escaped-html", "value": "john@evanswealthpartners.com"},
                               "link": {"$$type": "link", "value": {
                                   "destination": {"$$type": "url", "value": "mailto:john@evanswealthpartners.com"},
                                   "isTargetBlank": {"$$type": "boolean", "value": False}}}})

phone = widget("e-paragraph", {"classes": classes("ewp-text-link", "ewp-text-body"), "tag": S("p"),
                               "paragraph": {"$$type": "escaped-html", "value": "860-857-4770"},
                               "link": {"$$type": "link", "value": {
                                   "destination": {"$$type": "url", "value": "tel:+18608574770"},
                                   "isTargetBlank": {"$$type": "boolean", "value": False}}}})
phone_item = box(["ewp-contact-item"], [box(["ewp-icon-box"], [svg("ewp-icon-phone.svg", "ewp-icon")]),
                 box(["ewp-contact-item-body"], [para("Phone", "ewp-contact-label"), phone,
                     para("By appointment, 8am to 9pm, seven days a week.", "ewp-text-body")])])

# The form slot is deliberately empty: the client adds a working form here.
form_slot = box(["ewp-form-slot"], [], cssid="contact-form")
form_slot["editor_settings"] = {"title": "Contact form (empty: add your form here)"}

contact_sec = section(["ewp-section-intro", "ewp-section"], [
    box(["ewp-section-head"], [
        para("Contact", "ewp-eyebrow"),
        heading("Let's start with a conversation.", "h1", "ewp-title-page"),
        para("Tell us a little about where you are. We'll reply by the next business day to set up a 30-minute intro call, by phone or video.", "ewp-text-lead"),
    ]),
    box(["ewp-contact"], [
        form_slot,
        box(["ewp-contact-aside"], [
            image("river", "large", "ewp-photo-contact"),
            box(["ewp-contact-card"], [
                contact_item(image("portrait", "thumbnail", "ewp-photo-avatar"), "Who you'll talk to",
                             para("John Evans, founder. He takes every first call himself.", "ewp-text-body")),
                contact_item(box(["ewp-icon-box"], [svg("ewp-icon-mail.svg", "ewp-icon")]), "Email", email),
                phone_item,
                contact_item(box(["ewp-icon-box"], [svg("ewp-icon-map-pin.svg", "ewp-icon")]), "Where we meet",
                             para("Avon, the Farmington Valley, Connecticut and beyond. Most meetings are virtual, or we can meet at your home or your business.", "ewp-text-body")),
            ]),
            box(["ewp-contact-card"], [
                heading("What happens next", "h2", "ewp-title-card"),
                box(["ewp-next-list"], [box(["ewp-next-item"], [para(n, "ewp-next-number", tag="span"), para(t, "ewp-text-body")]) for n, t in [
                    ("1", "We reply by the next business day to book a time."),
                    ("2", "A 30-minute call about your situation and your questions."),
                    ("3", "If we're a good fit, we send a short list of documents for a discovery meeting."),
                ]]),
            ]),
        ], tag="aside"),
    ]),
], "contact")

faq_sec = faq_section([FAQ[k] for k in ["who", "first", "avon", "tax", "when"]], ["ewp-section-raised", "ewp-section"])

page = {"title": "Contact", "slug": "contact", "titles": ["Contact", "FAQ"], "elements": [contact_sec, faq_sec]}

defined = {c["label"] for c in CLASSES}
used = set()
def walk(e):
    used.update(e["settings"].get("classes", {}).get("value", []))
    for c in e["elements"]:
        walk(c)
walk(contact_sec)
assert used <= defined, used - defined
print("contact: classes used", len(used), "defined", len(defined))
new_svgs = ["ewp-icon-mail.svg", "ewp-icon-map-pin.svg"]
json.dump({"classes": CLASSES, "page": page, "svgs": {n: open("../assets/svg/" + n).read() for n in new_svgs}},
          open("contact_payload.json", "w"))
