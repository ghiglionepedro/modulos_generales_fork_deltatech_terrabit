# ©  2015-2020 Deltatech
#              Dorin Hongu <dhongu(@)gmail(.)com
# See README.rst file on addons root folder for license details
{
    "name": "eCommerce Category Snippet",
    "category": "Website",
    "summary": "eCommerce extension Category Snipped",
    "version": "14.0.1.0.0",
    "author": "Terrabit, Dorin Hongu",
    "license": "AGPL-3",
    "website": "https://www.terrabit.ro",
    "depends": ["website_sale", "deltatech_website_category"],
    "data": ["views/templates.xml", "views/snippets.xml", "data/website_data.xml"],
    "images": ["static/description/main_screenshot.png"],
    "installable": True,
    "qweb": ["static/src/xml/*.xml"],
    "development_status": "Mature",
    "maintainers": ["dhongu"],
}
