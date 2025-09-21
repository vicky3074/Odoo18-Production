{
    "name": "Clyvanta Professional Theme",
    "summary": "Custom professional theme for Clyvanta ERP - safe and stable",
    "version": "18.0.1.0.0",
    "category": "Website/Theme",
    "author": "Clyvanta",
    "license": "LGPL-3",
    "installable": True,
    "depends": ["web", "web_company_color"],
    "data": [],
    "assets": {
        "web.assets_backend": [
            "clyvanta_theme/static/src/scss/theme.scss",
            "clyvanta_theme/static/src/js/theme.js",
        ],
    },
    "auto_install": False,
    "application": False,
}