#!/bin/bash
curl -X POST -H 'Content-Type: application/json' https://arobertson.public.atlastunnel.com/bitbucket_push -d '{
    "push":
    {
        "changes":
        [
            {
                "forced": false,
                "old":
                {
                    "name": "master",
                    "links":
                    {
                        "commits":
                        {
                            "href": "https://api.bitbucket.org/2.0/repositories/aaronrobertson/connect-app/commits/master"
                        },
                        "self":
                        {
                            "href": "https://api.bitbucket.org/2.0/repositories/aaronrobertson/connect-app/refs/branches/master"
                        },
                        "html":
                        {
                            "href": "https://bitbucket.org/aaronrobertson/connect-app/branch/master"
                        }
                    },
                    "default_merge_strategy": "merge_commit",
                    "merge_strategies":
                    [
                        "merge_commit",
                        "squash",
                        "fast_forward"
                    ],
                    "type": "branch",
                    "target":
                    {
                        "rendered":
                        {},
                        "hash": "8317a0eb63890f0f62347884b485b6118515df3e",
                        "links":
                        {
                            "self":
                            {
                                "href": "https://api.bitbucket.org/2.0/repositories/aaronrobertson/connect-app/commit/8317a0eb63890f0f62347884b485b6118515df3e"
                            },
                            "html":
                            {
                                "href": "https://bitbucket.org/aaronrobertson/connect-app/commits/8317a0eb63890f0f62347884b485b6118515df3e"
                            }
                        },
                        "author":
                        {
                            "raw": "Aaron Robertson <arobertson@atlassian.com>",
                            "type": "author",
                            "user":
                            {
                                "display_name": "Aaron Robertson",
                                "uuid": "{20f4b4fe-43fb-4ff1-a7c6-b21a730e6505}",
                                "links":
                                {
                                    "self":
                                    {
                                        "href": "https://api.bitbucket.org/2.0/users/%7B20f4b4fe-43fb-4ff1-a7c6-b21a730e6505%7D"
                                    },
                                    "html":
                                    {
                                        "href": "https://bitbucket.org/%7B20f4b4fe-43fb-4ff1-a7c6-b21a730e6505%7D/"
                                    },
                                    "avatar":
                                    {
                                        "href": "https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/initials/AR-2.png"
                                    }
                                },
                                "type": "user",
                                "nickname": "Aaron Robertson",
                                "account_id": "6141f651e057c6006a36b01a"
                            }
                        },
                        "summary":
                        {
                            "raw": "3\n",
                            "markup": "markdown",
                            "html": "<p>3</p>",
                            "type": "rendered"
                        },
                        "parents":
                        [
                            {
                                "hash": "72fb4e80f6145d0d388292b2bf00a1f9ccffac9d",
                                "type": "commit",
                                "links":
                                {
                                    "self":
                                    {
                                        "href": "https://api.bitbucket.org/2.0/repositories/aaronrobertson/connect-app/commit/72fb4e80f6145d0d388292b2bf00a1f9ccffac9d"
                                    },
                                    "html":
                                    {
                                        "href": "https://bitbucket.org/aaronrobertson/connect-app/commits/72fb4e80f6145d0d388292b2bf00a1f9ccffac9d"
                                    }
                                }
                            }
                        ],
                        "date": "2021-10-06T04:11:19+00:00",
                        "message": "3\n",
                        "type": "commit",
                        "properties":
                        {}
                    }
                },
                "links":
                {
                    "commits":
                    {
                        "href": "https://api.bitbucket.org/2.0/repositories/aaronrobertson/connect-app/commits?include=f1cfc99b50658a61d1c2f158ae8b3625fc8f8b39&exclude=8317a0eb63890f0f62347884b485b6118515df3e"
                    },
                    "html":
                    {
                        "href": "https://bitbucket.org/aaronrobertson/connect-app/branches/compare/f1cfc99b50658a61d1c2f158ae8b3625fc8f8b39..8317a0eb63890f0f62347884b485b6118515df3e"
                    },
                    "diff":
                    {
                        "href": "https://api.bitbucket.org/2.0/repositories/aaronrobertson/connect-app/diff/f1cfc99b50658a61d1c2f158ae8b3625fc8f8b39..8317a0eb63890f0f62347884b485b6118515df3e"
                    }
                },
                "created": false,
                "commits":
                [
                    {
                        "rendered":
                        {},
                        "hash": "f1cfc99b50658a61d1c2f158ae8b3625fc8f8b39",
                        "links":
                        {
                            "self":
                            {
                                "href": "https://api.bitbucket.org/2.0/repositories/aaronrobertson/connect-app/commit/f1cfc99b50658a61d1c2f158ae8b3625fc8f8b39"
                            },
                            "comments":
                            {
                                "href": "https://api.bitbucket.org/2.0/repositories/aaronrobertson/connect-app/commit/f1cfc99b50658a61d1c2f158ae8b3625fc8f8b39/comments"
                            },
                            "patch":
                            {
                                "href": "https://api.bitbucket.org/2.0/repositories/aaronrobertson/connect-app/patch/f1cfc99b50658a61d1c2f158ae8b3625fc8f8b39"
                            },
                            "html":
                            {
                                "href": "https://bitbucket.org/aaronrobertson/connect-app/commits/f1cfc99b50658a61d1c2f158ae8b3625fc8f8b39"
                            },
                            "diff":
                            {
                                "href": "https://api.bitbucket.org/2.0/repositories/aaronrobertson/connect-app/diff/f1cfc99b50658a61d1c2f158ae8b3625fc8f8b39"
                            },
                            "approve":
                            {
                                "href": "https://api.bitbucket.org/2.0/repositories/aaronrobertson/connect-app/commit/f1cfc99b50658a61d1c2f158ae8b3625fc8f8b39/approve"
                            },
                            "statuses":
                            {
                                "href": "https://api.bitbucket.org/2.0/repositories/aaronrobertson/connect-app/commit/f1cfc99b50658a61d1c2f158ae8b3625fc8f8b39/statuses"
                            }
                        },
                        "author":
                        {
                            "raw": "Aaron Robertson <arobertson@atlassian.com>",
                            "type": "author",
                            "user":
                            {
                                "display_name": "Aaron Robertson",
                                "uuid": "{20f4b4fe-43fb-4ff1-a7c6-b21a730e6505}",
                                "links":
                                {
                                    "self":
                                    {
                                        "href": "https://api.bitbucket.org/2.0/users/%7B20f4b4fe-43fb-4ff1-a7c6-b21a730e6505%7D"
                                    },
                                    "html":
                                    {
                                        "href": "https://bitbucket.org/%7B20f4b4fe-43fb-4ff1-a7c6-b21a730e6505%7D/"
                                    },
                                    "avatar":
                                    {
                                        "href": "https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/initials/AR-2.png"
                                    }
                                },
                                "type": "user",
                                "nickname": "Aaron Robertson",
                                "account_id": "6141f651e057c6006a36b01a"
                            }
                        },
                        "summary":
                        {
                            "raw": "add token2\n",
                            "markup": "markdown",
                            "html": "<p>add token2</p>",
                            "type": "rendered"
                        },
                        "parents":
                        [
                            {
                                "hash": "a48c78e8152e698d063fd8ef203f1979e0e370d8",
                                "type": "commit",
                                "links":
                                {
                                    "self":
                                    {
                                        "href": "https://api.bitbucket.org/2.0/repositories/aaronrobertson/connect-app/commit/a48c78e8152e698d063fd8ef203f1979e0e370d8"
                                    },
                                    "html":
                                    {
                                        "href": "https://bitbucket.org/aaronrobertson/connect-app/commits/a48c78e8152e698d063fd8ef203f1979e0e370d8"
                                    }
                                }
                            }
                        ],
                        "date": "2021-10-07T00:16:49+00:00",
                        "message": "add token2\n",
                        "type": "commit",
                        "properties":
                        {}
                    },
                    {
                        "rendered":
                        {},
                        "hash": "a48c78e8152e698d063fd8ef203f1979e0e370d8",
                        "links":
                        {
                            "self":
                            {
                                "href": "https://api.bitbucket.org/2.0/repositories/aaronrobertson/connect-app/commit/a48c78e8152e698d063fd8ef203f1979e0e370d8"
                            },
                            "comments":
                            {
                                "href": "https://api.bitbucket.org/2.0/repositories/aaronrobertson/connect-app/commit/a48c78e8152e698d063fd8ef203f1979e0e370d8/comments"
                            },
                            "patch":
                            {
                                "href": "https://api.bitbucket.org/2.0/repositories/aaronrobertson/connect-app/patch/a48c78e8152e698d063fd8ef203f1979e0e370d8"
                            },
                            "html":
                            {
                                "href": "https://bitbucket.org/aaronrobertson/connect-app/commits/a48c78e8152e698d063fd8ef203f1979e0e370d8"
                            },
                            "diff":
                            {
                                "href": "https://api.bitbucket.org/2.0/repositories/aaronrobertson/connect-app/diff/a48c78e8152e698d063fd8ef203f1979e0e370d8"
                            },
                            "approve":
                            {
                                "href": "https://api.bitbucket.org/2.0/repositories/aaronrobertson/connect-app/commit/a48c78e8152e698d063fd8ef203f1979e0e370d8/approve"
                            },
                            "statuses":
                            {
                                "href": "https://api.bitbucket.org/2.0/repositories/aaronrobertson/connect-app/commit/a48c78e8152e698d063fd8ef203f1979e0e370d8/statuses"
                            }
                        },
                        "author":
                        {
                            "raw": "Aaron Robertson <arobertson@atlassian.com>",
                            "type": "author",
                            "user":
                            {
                                "display_name": "Aaron Robertson",
                                "uuid": "{20f4b4fe-43fb-4ff1-a7c6-b21a730e6505}",
                                "links":
                                {
                                    "self":
                                    {
                                        "href": "https://api.bitbucket.org/2.0/users/%7B20f4b4fe-43fb-4ff1-a7c6-b21a730e6505%7D"
                                    },
                                    "html":
                                    {
                                        "href": "https://bitbucket.org/%7B20f4b4fe-43fb-4ff1-a7c6-b21a730e6505%7D/"
                                    },
                                    "avatar":
                                    {
                                        "href": "https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/initials/AR-2.png"
                                    }
                                },
                                "type": "user",
                                "nickname": "Aaron Robertson",
                                "account_id": "6141f651e057c6006a36b01a"
                            }
                        },
                        "summary":
                        {
                            "raw": "add token1\n",
                            "markup": "markdown",
                            "html": "<p>add token1</p>",
                            "type": "rendered"
                        },
                        "parents":
                        [
                            {
                                "hash": "8317a0eb63890f0f62347884b485b6118515df3e",
                                "type": "commit",
                                "links":
                                {
                                    "self":
                                    {
                                        "href": "https://api.bitbucket.org/2.0/repositories/aaronrobertson/connect-app/commit/8317a0eb63890f0f62347884b485b6118515df3e"
                                    },
                                    "html":
                                    {
                                        "href": "https://bitbucket.org/aaronrobertson/connect-app/commits/8317a0eb63890f0f62347884b485b6118515df3e"
                                    }
                                }
                            }
                        ],
                        "date": "2021-10-07T00:16:16+00:00",
                        "message": "add token1\n",
                        "type": "commit",
                        "properties":
                        {}
                    }
                ],
                "truncated": false,
                "closed": false,
                "new":
                {
                    "name": "master",
                    "links":
                    {
                        "commits":
                        {
                            "href": "https://api.bitbucket.org/2.0/repositories/aaronrobertson/connect-app/commits/master"
                        },
                        "self":
                        {
                            "href": "https://api.bitbucket.org/2.0/repositories/aaronrobertson/connect-app/refs/branches/master"
                        },
                        "html":
                        {
                            "href": "https://bitbucket.org/aaronrobertson/connect-app/branch/master"
                        }
                    },
                    "default_merge_strategy": "merge_commit",
                    "merge_strategies":
                    [
                        "merge_commit",
                        "squash",
                        "fast_forward"
                    ],
                    "type": "branch",
                    "target":
                    {
                        "rendered":
                        {},
                        "hash": "f1cfc99b50658a61d1c2f158ae8b3625fc8f8b39",
                        "links":
                        {
                            "self":
                            {
                                "href": "https://api.bitbucket.org/2.0/repositories/aaronrobertson/connect-app/commit/f1cfc99b50658a61d1c2f158ae8b3625fc8f8b39"
                            },
                            "html":
                            {
                                "href": "https://bitbucket.org/aaronrobertson/connect-app/commits/f1cfc99b50658a61d1c2f158ae8b3625fc8f8b39"
                            }
                        },
                        "author":
                        {
                            "raw": "Aaron Robertson <arobertson@atlassian.com>",
                            "type": "author",
                            "user":
                            {
                                "display_name": "Aaron Robertson",
                                "uuid": "{20f4b4fe-43fb-4ff1-a7c6-b21a730e6505}",
                                "links":
                                {
                                    "self":
                                    {
                                        "href": "https://api.bitbucket.org/2.0/users/%7B20f4b4fe-43fb-4ff1-a7c6-b21a730e6505%7D"
                                    },
                                    "html":
                                    {
                                        "href": "https://bitbucket.org/%7B20f4b4fe-43fb-4ff1-a7c6-b21a730e6505%7D/"
                                    },
                                    "avatar":
                                    {
                                        "href": "https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/initials/AR-2.png"
                                    }
                                },
                                "type": "user",
                                "nickname": "Aaron Robertson",
                                "account_id": "6141f651e057c6006a36b01a"
                            }
                        },
                        "summary":
                        {
                            "raw": "add token2\n",
                            "markup": "markdown",
                            "html": "<p>add token2</p>",
                            "type": "rendered"
                        },
                        "parents":
                        [
                            {
                                "hash": "a48c78e8152e698d063fd8ef203f1979e0e370d8",
                                "type": "commit",
                                "links":
                                {
                                    "self":
                                    {
                                        "href": "https://api.bitbucket.org/2.0/repositories/aaronrobertson/connect-app/commit/a48c78e8152e698d063fd8ef203f1979e0e370d8"
                                    },
                                    "html":
                                    {
                                        "href": "https://bitbucket.org/aaronrobertson/connect-app/commits/a48c78e8152e698d063fd8ef203f1979e0e370d8"
                                    }
                                }
                            }
                        ],
                        "date": "2021-10-07T00:16:49+00:00",
                        "message": "add token2\n",
                        "type": "commit",
                        "properties":
                        {}
                    }
                }
            }
        ]
    },
    "actor":
    {
        "display_name": "Aaron Robertson",
        "uuid": "{20f4b4fe-43fb-4ff1-a7c6-b21a730e6505}",
        "links":
        {
            "self":
            {
                "href": "https://api.bitbucket.org/2.0/users/%7B20f4b4fe-43fb-4ff1-a7c6-b21a730e6505%7D"
            },
            "html":
            {
                "href": "https://bitbucket.org/%7B20f4b4fe-43fb-4ff1-a7c6-b21a730e6505%7D/"
            },
            "avatar":
            {
                "href": "https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/initials/AR-2.png"
            }
        },
        "type": "user",
        "nickname": "Aaron Robertson",
        "account_id": "6141f651e057c6006a36b01a"
    },
    "repository":
    {
        "scm": "git",
        "website": null,
        "uuid": "{3934fbca-7932-451b-8eda-cc1d61a7b850}",
        "links":
        {
            "self":
            {
                "href": "https://api.bitbucket.org/2.0/repositories/aaronrobertson/connect-app"
            },
            "html":
            {
                "href": "https://bitbucket.org/aaronrobertson/connect-app"
            },
            "avatar":
            {
                "href": "https://bytebucket.org/ravatar/%7B3934fbca-7932-451b-8eda-cc1d61a7b850%7D?ts=default"
            }
        },
        "project":
        {
            "links":
            {
                "self":
                {
                    "href": "https://api.bitbucket.org/2.0/workspaces/aaronrobertson/projects/ON"
                },
                "html":
                {
                    "href": "https://bitbucket.org/aaronrobertson/workspace/projects/ON"
                },
                "avatar":
                {
                    "href": "https://bitbucket.org/account/user/aaronrobertson/projects/ON/avatar/32?ts=1632797962"
                }
            },
            "type": "project",
            "name": "Onboarding",
            "key": "ON",
            "uuid": "{64083068-8937-47a2-9217-0228c051d585}"
        },
        "full_name": "aaronrobertson/connect-app",
        "owner":
        {
            "display_name": "Aaron Robertson",
            "uuid": "{20f4b4fe-43fb-4ff1-a7c6-b21a730e6505}",
            "links":
            {
                "self":
                {
                    "href": "https://api.bitbucket.org/2.0/users/%7B20f4b4fe-43fb-4ff1-a7c6-b21a730e6505%7D"
                },
                "html":
                {
                    "href": "https://bitbucket.org/%7B20f4b4fe-43fb-4ff1-a7c6-b21a730e6505%7D/"
                },
                "avatar":
                {
                    "href": "https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/initials/AR-2.png"
                }
            },
            "type": "user",
            "nickname": "Aaron Robertson",
            "account_id": "6141f651e057c6006a36b01a"
        },
        "workspace":
        {
            "slug": "aaronrobertson",
            "type": "workspace",
            "name": "Aaron Robertson",
            "links":
            {
                "self":
                {
                    "href": "https://api.bitbucket.org/2.0/workspaces/aaronrobertson"
                },
                "html":
                {
                    "href": "https://bitbucket.org/aaronrobertson/"
                },
                "avatar":
                {
                    "href": "https://bitbucket.org/workspaces/aaronrobertson/avatar/?ts=1632280857"
                }
            },
            "uuid": "{20f4b4fe-43fb-4ff1-a7c6-b21a730e6505}"
        },
        "type": "repository",
        "is_private": true,
        "name": "connect-app"
    }
}'
