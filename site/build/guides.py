"""The three Resources guides (approved copy from the compliance review doc, 10 Nov 2026).
Each becomes a child page of Resources: /resources/<slug>/.
Writes guides_payload.json: {classes, pages:[{title, slug, parent, titles, elements, seo}]}.
"""
from ewp_lib import *
import ewp_lib, json


def part(title, *children, cssid=None):
    return box(["ewp-article-part"], [heading(title, "h2", "ewp-title-section"), *children], cssid=cssid)


def guide_page(key, topic, minutes, title, lead, parts, note, sources, seo):
    ewp_lib.PAGE[0] = key
    intro = section(["ewp-section-intro", "ewp-section"], [
        box(["ewp-section-head"], [
            box(["ewp-card-meta"], [para(topic, "ewp-tag", tag="span"),
                                    para(f"{minutes} minute read", "ewp-text-small", tag="span"),
                                    para("Updated November 2026", "ewp-text-small", tag="span")]),
            heading(title, "h1", "ewp-title-page"),
            *[para(p, "ewp-text-lead") for p in lead],
        ]),
        box(["ewp-article"], [
            *parts,
            para(note, "ewp-service-note"),
            *([box(["ewp-article-part"], [para("Sources", "ewp-eyebrow"),
                                          *[text_link(t, u, "ewp-text-link", "ewp-text-small") for t, u in sources]])]
              if sources else []),
            link_arrow("All guides and worksheets", "/resources/"),
        ], tag="article"),
    ], "guide")
    booking = section(["ewp-section-booking", "ewp-section"], [
        box(["ewp-booking"], [
            box(["ewp-booking-copy"], [
                heading("Want to talk this through?", "h2", "ewp-title-section"),
                para("Book a free 30-minute call with John, by phone or video.", "ewp-text-body"),
            ]),
            button("Book an intro call", "/contact/", "ewp-button-primary", "ewp-button"),
        ]),
    ], "booking")
    return {"title": title, "slug": key, "parent": "resources", "titles": ["Guide", "Booking band"],
            "elements": [intro, booking], "seo": seo}


estate = guide_page(
    "connecticut-estate-and-gift-tax", "Estate", 3,
    "Connecticut's estate and gift tax, explained",
    ["Connecticut is the only state that taxes both estates and lifetime gifts. For 2026, the first $15 million of combined gifts and estate is exempt, which matches the federal exemption."],
    [
        part("Who has to think about it",
             para("Most families will never owe Connecticut estate tax. It matters if your home, retirement accounts, business, life insurance and investments together could pass $15 million, or if you expect them to grow toward that.", "ewp-text-body"),
             para("Life insurance counts toward your estate if you own the policy. Business owners are often surprised by how much the business adds.", "ewp-text-body")),
        part("How the tax works", bullets([
            "Exemption: $15 million per person in 2026, up from $13.99 million in 2025.",
            "Rate: 12% on the amount above the exemption.",
            "Cap: the most anyone pays in combined Connecticut estate and gift tax is $15 million.",
            "Lifetime gifts count: taxable gifts you make while alive use up the same $15 million. Gifts under the annual exclusion ($19,000 per person in 2026), and gifts to a spouse who is a US citizen, generally do not.",
        ])),
        part("Filing",
             para("Every Connecticut estate files a return, even when no tax is due. Estates under the exemption generally file with the local Probate Court. Larger estates file with the Department of Revenue Services. Returns for 2026 are due by April 15, 2027.", "ewp-text-body")),
        part("Questions to bring to your attorney and CPA", numbered([
            "Could our estate reach $15 million, counting the business and life insurance?",
            "Have we made gifts that used up part of our exemption?",
            "Should life insurance be owned by a trust instead of by us?",
            "Is our will or trust written so that both spouses' exemptions are used?",
        ])),
        part("How we help",
             para("We build an inventory of everything you own and what it may be worth when you are older. Then we work alongside your estate attorney and CPA, who give the legal and tax advice.", "ewp-text-body")),
    ],
    "Evans Wealth Partners does not provide legal or tax advice. Figures are for 2026 and change each year.",
    [("Connecticut Department of Revenue Services: Estate and Gift Tax Information",
      "https://portal.ct.gov/drs/individuals/individual-income-tax-portal/estate-and-gift-taxes/tax-information")],
    {"title": "Connecticut Estate and Gift Tax: A Plain-English Guide (2026)",
     "description": "How Connecticut's estate and gift tax works in 2026: the $15 million exemption, the 12% rate, why lifetime gifts count, and when a return is due."},
)

chet = guide_page(
    "connecticut-529-plan", "Planning", 2,
    "Connecticut's 529 plan (CHET) and the state tax deduction",
    ["Connecticut's 529 college savings plan is called CHET, the Connecticut Higher Education Trust. Contributions can lower your Connecticut income tax, and the money grows free of federal and state income tax when it is spent on qualified education costs."],
    [
        part("The Connecticut tax deduction", bullets([
            "Up to $5,000 a year for a single filer, or $10,000 for a married couple filing jointly.",
            "The limit is per taxpayer, not per child. Two children's accounts still share the same $5,000 or $10,000.",
            "Put in more, deduct it later: contributions above the limit can be carried forward and deducted over the next five years.",
        ])),
        part("Who can open one",
             para("Parents, grandparents, other relatives and friends can open a CHET account for a child. The account owner keeps control of the money, not the child.", "ewp-text-body")),
        part("Things families often miss", bullets([
            "Grandparents in Connecticut can take the deduction on their own return for their own contributions.",
            "If the money is not used for education, earnings are taxed and usually face a 10% federal penalty. Connecticut may also take back deductions it allowed.",
        ])),
        part("How we help",
             para("We fit college saving into your whole plan, so it does not come at the cost of your own retirement. That matters most for parents saving for both at the same time.", "ewp-text-body")),
    ],
    "Evans Wealth Partners does not provide legal or tax advice. Check the plan's offering documents before investing; they describe its fees, risks and investment options.",
    [("CHET 529 College Savings Plan: plan details", "https://www.aboutchet.com/plan/details.shtml"),
     ("Connecticut General Assembly: State tax deduction for CHET contributions", "https://www.cga.ct.gov/2008/rpt/2008-R-0061.htm")],
    {"title": "Connecticut 529 Plan (CHET): Tax Deduction and How It Works",
     "description": "How Connecticut's CHET 529 plan works: the state income tax deduction of up to $5,000 or $10,000 a year, the five-year carryforward, and tips for parents and grandparents."},
)

business = guide_page(
    "selling-your-business", "Business owners", 3,
    "Selling your business in the next ten years? Start here.",
    ["The best time to plan a sale is three to five years before you want out. That gives you time to make the business easier to buy, and to settle the tax questions while you still have choices."],
    [
        part("What buyers look at", bullets([
            "Clean, consistent financials: several years of accounts that a buyer's accountant can follow without surprises.",
            "How much the business depends on you. If customers, suppliers and staff only deal with the owner, buyers pay less or ask you to stay on longer.",
            "Customer concentration. One customer making up a large share of sales is a risk buyers price in.",
            "Recurring revenue and a team that can run things. Both make the business worth more to someone else.",
        ])),
        part("How long a sale takes",
             para("Getting the business ready often takes years, not months. The sale itself, from first conversations to closing, commonly runs many months. Owners who start early can choose their timing instead of selling because of health, a partner leaving or a slow market.", "ewp-text-body")),
        part("Tax questions to settle before you sign a letter of intent",
             numbered([
                 "Is the deal a sale of the company's shares or of its assets? The answer changes how the proceeds are taxed.",
                 "How will the price be split between equipment, goodwill and any agreement for you to stay on or not compete?",
                 "Will you be paid all at once, over time, or partly on future results?",
                 "How will the proceeds fit with your retirement, your estate plan and Connecticut's estate and gift tax?",
             ]),
             para("Once a letter of intent is signed, many of these points are much harder to change.", "ewp-text-body")),
        part("If you have partners: buy-sell agreements and key person cover",
             para("A buy-sell agreement says what happens to an owner's share if they die, become disabled, retire or leave. Life insurance is often used to pay for it, so the remaining owners can buy the share and the family receives fair value. Key person insurance protects the business if someone it relies on dies.", "ewp-text-body"),
             para("Review these when the business's value changes. An agreement written years ago at an old valuation can leave a family or the remaining partners short.", "ewp-text-body"),
             cssid="buy-sell"),
        part("How we help",
             para("John has run a pub, a health club and a coaching business, so he has been the owner on the other side of the table. We plan the sale alongside your household finances and work with your attorney, CPA and any business broker.", "ewp-text-body")),
    ],
    "Evans Wealth Partners does not provide legal or tax advice. We work alongside your attorney and CPA.",
    [],
    {"title": "Selling Your Business: A Succession Planning Guide for Connecticut Owners",
     "description": "What buyers look at, how long a sale usually takes, and the tax questions to settle before you sign a letter of intent. A plain-English guide for business owners."},
)

pages = [estate, chet, business]
defined = {c["label"] for c in CLASSES}
used = set()
def walk(e):
    used.update(e["settings"].get("classes", {}).get("value", []))
    for c in e["elements"]:
        walk(c)
for p in pages:
    for e in p["elements"]:
        walk(e)
assert used <= defined, used - defined
print("guides: classes used", len(used), "defined", len(defined))
json.dump({"classes": CLASSES, "pages": pages}, open("guides_payload.json", "w"))
