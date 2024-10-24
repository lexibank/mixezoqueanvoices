from setuptools import setup
import json


with open('metadata.json', encoding='utf-8') as fp:
    metadata = json.load(fp)


setup(
    name='lexibank_mixezoqueanvoices',
    description=metadata['title'],
    license=metadata.get('license', ''),
    url=metadata.get('url', ''),
    py_modules=['lexibank_mixezoqueanvoices'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'lexibank.dataset': [
            'mixezoqueanvoices=lexibank_mixezoqueanvoices:Dataset',
        ],
        "cldfbench.commands": [
            "mixezoqueanvoices=mixezoqueanvoices_subcommands",
        ]
    },
    install_requires=[
        'pylexibank>=3.3.0',
        'cldfbench>=1.7.2',
        'zenodoclient>=0.4.1',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
