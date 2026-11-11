from ewp_lib import *
import ewp_lib, json
ewp_lib.PAGE[0] = "services"

def bullet_list(items):
    return box(["ewp-bullet-list"], [
        box(["ewp-bullet-item"], [svg("ewp-bullet-square.svg", "ewp-bullet-dot"), para(t, "ewp-text-body", tag="span")])
        for t in items])

def detail_col(title, items):
    return box(["ewp-detail-col"], [heading(title, "h3", "ewp-detail-title"), bullet_list(items)])

def service_block(anchor, icon, eyebrow, title, body, look, get):
    return box(["ewp-service-block"], [
        box(["ewp-service-intro"], [
            box(["ewp-icon-box"], [svg(icon, "ewp-icon")]),
            para(eyebrow, "ewp-eyebrow"),
            heading(title, "h2", "ewp-title-section"),
            para(body, "ewp-text-body"),
        ]),
        box(["ewp-service-detail"], [detail_col("What we look at", look), detail_col("What you get", get)]),
    ], tag="article", cssid=anchor)

pills = [("Financial planning", "planning"), ("Retirement planning", "retirement"), ("Investments", "investments"),
         ("Protection strategies", "protection"), ("Income strategies", "income"), ("Estate planning", "estate"),
         ("Business planning", "business-planning")]

# 1. Intro
intro_sec = section(["ewp-section-intro", "ewp-section"], [
    box(["ewp-section-head"], [
        para("Services", "ewp-eyebrow"),
        heading("Seven areas of advice, held together by one plan.", "h1", "ewp-title-page"),
        para("Most families end up with an advisor for investments, an agent for insurance and an attorney for the will, and nobody looking at the whole picture. We start with your plan and make every piece answer to it.", "ewp-text-lead"),
    ]),
    box(["ewp-pill-list"], [button(t, f"/services/#{a}", "ewp-pill") for t, a in pills], tag="nav"),
    image("banner", "full", "ewp-photo-wide"),
], "intro")

# 2. Service blocks
blocks = [
    ("planning", "ewp-icon-plan-map.svg", "Where every client starts", "Financial planning",
     "Your plan is a written document that pulls everything into one place: what you earn, spend, own and owe, and what you want. It shows whether your goals are on track and what to change if they aren't.",
     ["Cash flow, spending and savings rate", "Your goals, with dates and price tags", "Your tax position, alongside your CPA", "Your business and household balance sheets"],
     ["A written plan and a one-page summary", "A short list of next steps, in order", "A yearly review, and updates when life changes"]),
    ("retirement", "ewp-icon-retirement-sunset.svg", "When can you stop?", "Retirement planning",
     "We build your retirement around the life you want, then test it against good markets and bad ones. You'll know how much room you have before you hand in your notice.",
     ["Your target date and expected spending", "When to claim Social Security", "401(k), IRA and pension choices", "Health cover before Medicare starts at 65"],
     ["A retirement date range you can plan around", "A savings target for each year until then", "A Social Security claiming recommendation"]),
    ("investments", "ewp-icon-investments-pie.svg", "Money with a job to do", "Investments",
     "We invest to your timeline and to the level of risk your plan needs, not to the headlines. Your accounts are managed together, so each investment sits where it is taxed least.",
     ["The risk you need to take, and the risk you can live with", "What belongs in taxable, IRA and Roth accounts", "Fund costs and fees", "Large single holdings, including company stock"],
     ["A written investment policy statement", "Regular rebalancing back to your targets", "Reports you can read in five minutes"]),
    ("protection", "ewp-icon-protection-shield.svg", "Cover for what would really hurt", "Protection strategies",
     "Insurance should fill specific gaps in your plan. We review what you already own before suggesting anything new, and we size any new cover to real numbers.",
     ["Life cover to replace income and clear debts", "Disability cover for your earning power", "The cost of long-term care", "Buy-sell funding and key person cover"],
     ["A review of every policy you already hold", "A list of gaps, in dollars", "Options compared side by side when cover is needed"]),
    ("income", "ewp-icon-income-banknote.svg", "A paycheck from your savings", "Income strategies",
     "When the salary stops, someone has to decide which account pays the bills each month. We plan that order so more of what you saved stays yours.",
     ["Which accounts to draw from first", "Roth conversions in lower-tax years", "Required minimum distributions", "Where an annuity might fit, and where it doesn't"],
     ["A monthly income map for your first ten years", "A tax plan for your withdrawals", "A cash reserve, so a bad market never forces a sale"]),
    ("estate", "ewp-icon-estate-house.svg", "Passing on what you've built", "Estate planning",
     "We aren't attorneys and we don't draft legal documents. We work with your estate attorney so your plan, your paperwork and your accounts all say the same thing.",
     ["Beneficiaries on every account and policy", "Wills, trusts and powers of attorney", "Connecticut estate and gift tax", "Succession for a family business"],
     ["A one-page map of who receives what", "A beneficiary check on every account", "One plan shared with your attorney and CPA"]),
]
list_sec = section(["ewp-section-raised", "ewp-section"], [
    box(["ewp-service-list"], [service_block(*b) for b in blocks] + [
        para("Evans Wealth Partners does not provide legal or tax advice. We work alongside your attorney and CPA.", "ewp-service-note"),
    ]),
], "services")

# 3. Business planning (navy)
biz_cards = [
    ("ewp-icon-employees.svg", "Employee plans and benefits", "401(k), SEP IRA and SIMPLE IRA plans, and the benefits package around them, chosen for your size, your staff and your budget."),
    ("ewp-icon-income-banknote.svg", "Cash management", "Operating cash, reserves and surplus kept in the right places, so the business has what it needs and spare cash isn't left sitting idle."),
    ("ewp-icon-risk-warning.svg", "Risk management", "A clear look at what could hurt the business, from liability and property to losing a key person, and how each risk is covered."),
    ("ewp-icon-business-briefcase.svg", "Business structure and tax efficiency", "Whether your LLC, S corporation or partnership still fits, and how you pay yourself, worked out with your CPA."),
    ("ewp-icon-costs-document.svg", "Buy-sell agreements", "An agreement between owners that says what happens if one dies, becomes disabled or leaves, and the money to carry it out."),
    ("ewp-icon-succession-exit.svg", "Succession and exit planning", "A plan for handing the business to family, a partner or your team, or for selling it, years before the day comes."),
    ("ewp-icon-liquidity-coins.svg", "Liquidity events", "When the business sells or a large payout lands, a plan for the taxes, the investments and what you'll live on afterwards."),
    ("ewp-icon-key-person.svg", "Key person insurance", "Cover that protects the business if an owner, or someone it can't easily replace, dies or becomes seriously ill."),
]
biz_sec = box(["ewp-section-navy", "ewp-section"], [box(["ewp-wrap"], [
    box(["ewp-section-head"], [
        box(["ewp-icon-box-on-navy", "ewp-icon-box"], [svg("ewp-icon-business-briefcase.svg", "ewp-icon")]),
        para("For business owners", "ewp-eyebrow-on-navy", "ewp-eyebrow"),
        heading("Business planning", "h2", "ewp-title-on-navy", "ewp-title-section"),
        para("Your business is probably your biggest asset and your biggest risk. We plan it alongside your household, so a decision in one never quietly costs the other. John has run a pub, a health club and a coaching business. He'll talk to you like an owner, because he was one.", "ewp-text-on-navy", "ewp-text-lead"),
    ]),
    box(["ewp-card-list"], [box(["ewp-card-principle", "ewp-card-raised"], [
        box(["ewp-icon-box-on-navy", "ewp-icon-box"], [svg(ic, "ewp-icon")]),
        heading(t, "h3", "ewp-title-on-navy", "ewp-title-card"),
        para(b, "ewp-text-on-navy-muted", "ewp-text-body"),
    ], tag="article") for ic, t, b in biz_cards]),
    box(["ewp-action-row"], [button("Book an owner's call", "/contact/", "ewp-button-primary", "ewp-button")]),
])], tag="section", cssid="business-planning")

# 4. Booking band
booking_sec = section(["ewp-section-booking", "ewp-section"], [
    box(["ewp-booking"], [
        box(["ewp-booking-copy"], [
            heading("Not sure where to start?", "h2", "ewp-title-section"),
            para("Most people aren't. Book a 30-minute call and we'll tell you which of these matters most for you right now.", "ewp-text-body"),
        ]),
        button("Book an intro call", "/contact/", "ewp-button-primary", "ewp-button"),
    ]),
], "booking")

page = {"title": "Services", "slug": "services",
        "titles": ["Intro", "Service details", "Business planning", "Booking band"],
        "elements": [intro_sec, list_sec, biz_sec, booking_sec]}

defined = {c["label"] for c in CLASSES}
used = set()
def walk(e):
    used.update(e["settings"].get("classes", {}).get("value", []))
    for c in e["elements"]:
        walk(c)
for e in page["elements"]:
    walk(e)
assert used <= defined, used - defined
print("services: classes used", len(used), "defined", len(defined))
new_svgs = ["ewp-icon-employees.svg", "ewp-icon-risk-warning.svg", "ewp-icon-succession-exit.svg", "ewp-icon-liquidity-coins.svg", "ewp-icon-key-person.svg"]
json.dump({"classes": CLASSES, "page": page, "svgs": {n: open("../assets/svg/" + n).read() for n in new_svgs}},
          open("services_payload.json", "w"))
