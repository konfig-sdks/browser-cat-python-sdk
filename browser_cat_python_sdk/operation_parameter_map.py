operation_parameter_map = {
    '/auth/keys-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'role'
            },
            {
                'name': 'expiredAt'
            },
        ]
    },
    '/auth/keys/{keyId}-GET': {
        'parameters': [
            {
                'name': 'keyId'
            },
        ]
    },
    '/auth/keys-GET': {
        'parameters': [
        ]
    },
    '/auth/keys/{keyId}-DELETE': {
        'parameters': [
            {
                'name': 'keyId'
            },
        ]
    },
    '/auth/keys/{keyId}-PUT': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'role'
            },
            {
                'name': 'expiredAt'
            },
            {
                'name': 'keyId'
            },
        ]
    },
    '/auth/keys/{keyId}-PATCH': {
        'parameters': [
            {
                'name': 'keyId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'role'
            },
            {
                'name': 'expiredAt'
            },
        ]
    },
    '/billing/subscriptions/current-GET': {
        'parameters': [
        ]
    },
    '/billing/invoices/{invId}.pdf-GET': {
        'parameters': [
            {
                'name': 'invId'
            },
        ]
    },
    '/billing/invoices/{invId}-GET': {
        'parameters': [
            {
                'name': 'invId'
            },
        ]
    },
    '/billing/subscriptions/{subId}-GET': {
        'parameters': [
            {
                'name': 'subId'
            },
        ]
    },
    '/billing/invoices-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'afterDate'
            },
            {
                'name': 'beforeDate'
            },
        ]
    },
    '/billing/subscriptions-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'afterDate'
            },
            {
                'name': 'beforeDate'
            },
        ]
    },
    '/connect-GET': {
        'parameters': [
            {
                'name': 'region'
            },
        ]
    },
    '/openapi-GET': {
        'parameters': [
        ]
    },
    '/openapi.json-GET': {
        'parameters': [
        ]
    },
    '/openapi.yaml-GET': {
        'parameters': [
        ]
    },
    '/health-GET': {
        'parameters': [
        ]
    },
    '/metrics-GET': {
        'parameters': [
        ]
    },
    '/usage/sessions/{sessionId}/events/{eventId}-GET': {
        'parameters': [
            {
                'name': 'sessionId'
            },
            {
                'name': 'eventId'
            },
        ]
    },
    '/usage/sessions/{sessionId}-GET': {
        'parameters': [
            {
                'name': 'sessionId'
            },
        ]
    },
    '/usage/sessions-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'afterDate'
            },
            {
                'name': 'beforeDate'
            },
        ]
    },
    '/usage/buckets-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'afterDate'
            },
            {
                'name': 'beforeDate'
            },
            {
                'name': 'unit'
            },
            {
                'name': 'userId'
            },
            {
                'name': 'keyId'
            },
            {
                'name': 'method'
            },
            {
                'name': 'endpoint'
            },
        ]
    },
    '/usage/sessions/{sessionId}/events-GET': {
        'parameters': [
            {
                'name': 'sessionId'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'afterDate'
            },
            {
                'name': 'beforeDate'
            },
        ]
    },
};