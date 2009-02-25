# -*- coding: utf-8 -*-
#
# gPodder - A media aggregator and podcast client
# Copyright (c) 2005-2009 Thomas Perl and the gPodder Team
#
# gPodder is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# gPodder is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

# The User-Agent string for downloads
user_agent = 'gPodder'

# Interface type enums
(CLI, GUI, MAEMO) = range(3)

# Are we running in GUI, Maemo or console mode?
interface = CLI

# D-Bus specific interface names
dbus_bus_name = 'org.godder'
dbus_gui_object_path = '/gui'
dbus_interface = 'org.gpodder.interface'

