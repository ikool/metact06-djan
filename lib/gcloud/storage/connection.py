# Copyright 2014 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Create / interact with gcloud storage connections."""

from gcloud import connection as base_connection


SCOPE = ('https://www.googleapis.com/auth/devstorage.full_control',
         'https://www.googleapis.com/auth/devstorage.read_only',
         'https://www.googleapis.com/auth/devstorage.read_write')
"""The scopes required for authenticating as a Cloud Storage consumer."""


class Connection(base_connection.JSONConnection):
    """A connection to Google Cloud Storage via the JSON REST API."""

    API_BASE_URL = base_connection.API_BASE_URL
    """The base of the API call URL."""

    API_VERSION = 'v1'
    """The version of the API, used in building the API call's URL."""

    API_URL_TEMPLATE = '{api_base_url}/storage/{api_version}{path}'
    """A template for the URL of a particular API call."""

    def __init__(self, credentials=None, http=None):
        credentials = self._create_scoped_credentials(credentials, SCOPE)
        super(Connection, self).__init__(credentials=credentials, http=http)
