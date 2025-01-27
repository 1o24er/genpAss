# coding=utf-8

rules = [
    '{qq}',
    '{name}',
    '{username}',
    '{company}',
    '{birthday}',
    '{mobile}',

    '{username}.',
    '{username}!',
    '{username}!0123',
    '{username}123',

    '{company}123',
    '{company}1234',
    '{company}12345',
    '{company}2014',
    '{company}2008',
    '{company}#123',
    '{company}@123',
    '{company}@2014',
    '{company}@2015',
    '{company}1q2w3e4r',
    '{company}1q2w3e4r5t',

    'QQ{qq}',
    'qq{qq}',
    '{qq}@{name}',

    '{username}@{company}',
    '{username}#{company}',
    '{name}@{company}',
    '{name}#{company}',

    '{name}{qq}',
    '{name}{birthday}',
    '{birthday}{name}',

    '{name}{mobile}',
]
