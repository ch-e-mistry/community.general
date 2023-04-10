# Copyright (c) 2016-2017 Hewlett Packard Enterprise Development LP
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import sys
from ansible_collections.community.general.tests.unit.compat.mock import Mock

# FIXME: These should be done inside of a fixture so that they're only mocked during
# these unittests
if 'hpOneView' not in sys.modules:
    sys.modules['hpOneView'] = Mock()
    sys.modules['hpOneView.oneview_client'] = Mock()

ONEVIEW_MODULE_UTILS_PATH = 'ansible_collections.community.general.plugins.module_utils.oneview'
from ansible_collections.community.general.plugins.module_utils.oneview import (  # noqa: F401, pylint: disable=unused-import
    OneViewModuleException,
    OneViewModuleTaskError,
    OneViewModuleResourceNotFound,
    OneViewModuleBase,
)

from ansible_collections.community.general.plugins.modules.remote_management.oneview.oneview_ethernet_network import ( \
    # noqa: F401, pylint: disable=unused-import
    EthernetNetworkModule
)
from ansible_collections.community.general.plugins.modules.remote_management.oneview.oneview_ethernet_network_info import ( \
    # noqa: F401, pylint: disable=unused-import
    EthernetNetworkInfoModule
)
from ansible_collections.community.general.plugins.modules.remote_management.oneview.oneview_fc_network import ( \
    # noqa: F401, pylint: disable=unused-import
    FcNetworkModule
)
from ansible_collections.community.general.plugins.modules.remote_management.oneview.oneview_fc_network_info import ( \
    # noqa: F401, pylint: disable=unused-import
    FcNetworkInfoModule
)
from ansible_collections.community.general.plugins.modules.remote_management.oneview.oneview_fcoe_network import ( \
    # noqa: F401, pylint: disable=unused-import
    FcoeNetworkModule
)
from ansible_collections.community.general.plugins.modules.remote_management.oneview.oneview_fcoe_network_info import ( \
    # noqa: F401, pylint: disable=unused-import
    FcoeNetworkInfoModule
)
from ansible_collections.community.general.plugins.modules.remote_management.oneview.oneview_network_set import ( \
    # noqa: F401, pylint: disable=unused-import
    NetworkSetModule
)
from ansible_collections.community.general.plugins.modules.remote_management.oneview.oneview_network_set_info import ( \
    # noqa: F401, pylint: disable=unused-import
    NetworkSetInfoModule
)
from ansible_collections.community.general.plugins.modules.remote_management.oneview.oneview_san_manager import ( \
    # noqa: F401, pylint: disable=unused-import
    SanManagerModule
)
from ansible_collections.community.general.plugins.modules.remote_management.oneview.oneview_san_manager_info import ( \
    # noqa: F401, pylint: disable=unused-import
    SanManagerInfoModule
)