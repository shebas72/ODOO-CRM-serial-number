{
    'name': 'CRM Serial Number',
    'version': '1.0',
    'category': 'Sales/CRM',
    'summary': 'Auto-generate serial numbers for CRM Opportunities',
    'description': 'Automatically assign serial numbers to CRM leads (opportunities) using a sequence.',
    'author': 'Shebas Khan',
    'depends': ['crm'],
    'data': [
        'data/sequence.xml',
        'views/crm_lead_views.xml',
    ],
    'installable': True,
    'application': False,
}
