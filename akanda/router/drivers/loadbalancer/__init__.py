# Copyright (c) 2015 Akanda, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


from akanda.router.drivers.loadbalancer import nginx

# XXX move to config
CONFIGURED_LB_DRIVER = 'nginx'

AVAILABLE_DRIVERS = {
    'nginx': nginx.NginxLB,
    'nginx+': nginx.NginxPlusLB,
    # 'haxproxy': HaProxyLB,
}


class InvalidDriverException(Exception):
    pass


def get_loadbalancer_driver(name):
    try:
        return AVAILABLE_DRIVERS[name]
    except KeyError:
        raise InvalidDriverException(
            'Could not find LB driver by name %s' % name)
