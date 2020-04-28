

class UserInfo:

    #{'login': 'bmwill', 'id': 6741899, 'node_id': 'MDQ6VXNlcjY3NDE4OTk=', 'avatar_url': 'https://avatars1.githubusercontent.com/u/6741899?v=4', 'gravatar_id': '', 'url': 'https://api.github.com/users/bmwill', 'html_url': 'https://github.com/bmwill', 'followers_url': 'https://api.github.com/users/bmwill/followers', 'following_url': 'https://api.github.com/users/bmwill/following{/other_user}', 'gists_url': 'https://api.github.com/users/bmwill/gists{/gist_id}', 'starred_url': 'https://api.github.com/users/bmwill/starred{/owner}{/repo}', 'subscriptions_url': 'https://api.github.com/users/bmwill/subscriptions', 'organizations_url': 'https://api.github.com/users/bmwill/orgs', 'repos_url': 'https://api.github.com/users/bmwill/repos', 'events_url': 'https://api.github.com/users/bmwill/events{/privacy}', 'received_events_url': 'https://api.github.com/users/bmwill/received_events', 'type': 'User', 'site_admin': 'False', 'contributions': 377}
    def __init__(self,login,id,node_id,avatar_url,gravatar_id,url,html_url,followers_url,following_url,gists_url,starred_url,subscriptions_url,organizations_url,repos_url,events_url,received_events_url,type,site_admin,contributions):
        self.login = login
        self.id = id
        self.node_id = node_id
        self.avatar_url = avatar_url
        self.gravatar_id = gravatar_id
        self.url = url
        self.html_url = html_url
        self.followers_url = followers_url.split('{')[0]
        self.following_url = following_url.split('{')[0]
        self.gists_url = gists_url.replace('{','').replace('}','')
        self.starred_url = starred_url.split('{')[0]
        self.subscriptions_url = subscriptions_url
        self.organizations_url = organizations_url
        self.repos_url = repos_url
        self.events_url = events_url.split('{')[0]
        self.received_events_url = received_events_url
        self.type = type
        self.site_admin = site_admin
        self.contributions = contributions



    def __str__(self):
        return f'''\n {self.__dict__}'''

    def __repr__(self):
        return str(self)

