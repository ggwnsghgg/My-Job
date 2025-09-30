# -*- coding: utf-8 -*-
{
    'name': 'Auth Signup with Code Verification',
    'version': '1.0',
    'category': 'Extra Tools',
    'summary': """Enhance Odoo's signup process with code verification for secure and user-friendly registration.""",
    'description': """
The 'Auth Signup with Code Verification' module extends Odoo's default signup functionality 
by adding code-based verification. This allows users to validate their signup process through 
an email verification code.

**Key Features:**
- Secure email-based code verification during signup
- JSON-based API support for validation
- Enhanced error handling for invalid or expired codes
- Easy integration with existing authentication flows

Perfect for businesses requiring enhanced security during user onboarding.
    """,
    'author': 'Linkup Infotech Inc.',
    'website': 'https://www.link-up.co.kr',
    'depends': ['auth_signup'],
    'data': [
        'data/mail_template_data.xml',
        'views/auth_signup_login_templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'lu_auth_signup_code/static/src/js/**/*',
        ],
    },
    'images': ['static/description/banner.png'],
    'price': 20,
    'currency': 'USD',
    'license': 'Other proprietary',
}
