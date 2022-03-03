"""
Example data to start the database
"""
DEFAULT_HIRING_STAGES = [
    'Applied',
    'Resume Analysis',
    'Contacted',
    'Interview',
    'Interview Done',
    'Offer Draft',
    'Offered',
    'Offer Accepted',
    'Offer Declined',
    'Hired'
]

JOB_BENEFITS = [
    {
    'name': 'Health Insurance',
    },
    {
    'name': 'Disability Insurance',
    },
    {
    'name': 'Life Insurance',
    },
    {
    'name': 'Paid Time Off (PTO)',
    },
    {
    'name': 'Tuiton Assistance',
    },
    {
    'name': 'Parental Leaving',
    },
    {
    'name:' 'Remote work',
    },
]

HIRING_TYPES = [
    'Full time',
    'Part time',
    'Contract',
    'Temporary',
    'Internship'
]

HIRING_STAGES = [
    'Published',
    'Internal',
    'Private',
    'On Hold',
    'Closed',
    'Deleted'
]

CANDIDATES = [
    {
        'id': 1,
        'name': 'Michelangelo Tartaruga Ninja',
        'address': 'Boeiro de Rua, 1, New York, NY, USA',
        'phone': '+1 (212) 846-2543',
        'linkedin': 'www.linkedin.com/michelangelo',
        'applied_on': 'December 10, 1815',
        'stage': 'Applied',
        'last_modified_on': 'December 10, 1815',
        'email': 'michelangelo@tmnt.com',
    },
    {
        'id': 2,
        'name': 'Leonardo Tartaruga Ninja',
        'address': 'Boeiro de Rua, 1, New York, NY, USA',
        'phone': '+1 (212) 846-2543',
        'linkedin': 'www.linkedin.com/leonardo',
        'applied_on': 'December 10, 1815',
        'stage': 'Contacted',
        'last_modified_on': 'December 10, 1815',
        'email': 'leonardo@tmnt.com',
    },
    {
        'id': 3,
        'name': 'Rafael Tartaruga Ninja',
        'address': 'Boeiro de Rua, 1, New York, NY, USA',
        'phone': '+1 (212) 846-2543',
        'linkedin': 'www.linkedin.com/rafael',
        'applied_on': 'December 10, 1815',
        'stage': 'Resume Analysis',
        'last_modified_on': 'December 10, 1815',
        'email': 'rafael@tmnt.com',
    },
    {
        'id': 4,
        'name': 'Donatello Tartaruga Ninja',
        'address': 'Boeiro de Rua, 1, New York, NY, USA',
        'phone': '+1 (212) 846-2543',
        'linkedin': 'www.linkedin.com/donatello',
        'applied_on': 'December 10, 1815',
        'stage': 'Interview Done',
        'last_modified_on': 'December 10, 1815',
        'email': 'donatello@tmnt.com',
    },
    {
        'id': 5,
        'name': 'Senhor Splinter Rato',
        'address': 'Boeiro de Rua, 1, New York, NY, USA',
        'phone': '+1 (212) 846-2543',
        'linkedin': 'www.linkedin.com/splinter',
        'applied_on': 'December 10, 1815',
        'stage': 'Applied',
        'last_modified_on': 'December 10, 1815',
        'email': 'splinter@tmnt.com',
    },
]

OFFICES = [
    {
        'title': 'Headquarter',
        'address': '1515 Broadway New York, New York 10036 ',
        'phone': '+1 (201) 766-7329'
    },
    {
        'title': 'Office 1',
        'address': '',
        'phone': '+1 (212) 846-6006'
    },
    {
        'title': 'Office 2',
        'address': '17 - 29 Hawley Crescent, Camden, London NW1 8TT',
        'phone': '+1 (212) 846-6007'
    },
]

JOB_POSTINGS = [
    {
        'title': 'Quality Assurance',
        'description': 'A quality assurance specialist ensures that the final product observes the company\'s quality standards. In general, these detail-oriented professionals are responsible for the development and implementation of inspection activities, the detection and resolution of problems, and the delivery of satisfactory outcomes.',
        'salary_min': 1000,
        'salary_max': 5000,
    },
    {
        'title': 'Recruiter',
        'description': 'Recruiters are responsible for meet hiring goals by filling open positions with talented and qualified candidates. This entails sourcing and screening candidates, coordinating the interview process, and facilitating offers and employment negotiations, all while ensuring candidates have a pleasant experience.',
        'salary_min': 2000,
        'salary_max': 2500,
    },
    {
        'title': 'Baker',
        'description': 'Prepares, produces, and bakes breakfast pastries, breads, rolls, and some desserts. Develops new products for a la carte or menus on a rotating basis. Decorates baked goods, such as cream pies, using a pastry bag.',
        'salary_min': 500,
        'salary_max': 6500,
    },
    {
        'title': 'Car Salesman',
        'description': 'A Car Salesperson, or Auto Sales Representative, is responsible for selling cars, trucks and vans for personal and commercial use. Their duties include meeting with customers to discuss their needs, promoting sales offers at their dealership and participating in test drives with interested customers.',
        'salary_min': 4000,
        'salary_max': 10000,
    },
]
