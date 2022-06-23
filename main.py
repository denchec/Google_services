import google_auth_oauthlib.flow as fl


def main():
    flow = fl.Flow.from_client_secrets_file('client_secret.json',
                                            scopes=['https://www.googleapis.com/auth/spreadsheets.readonly'])

    flow.redirect_uri = 'http://localhost:49585/'

    authorization_url, state = flow.authorization_url(access_type='offline', include_granted_scopes='true')

    print(authorization_url)


if __name__ == '__main__':
    main()
