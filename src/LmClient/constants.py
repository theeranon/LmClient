"""
@summary: Constants for the Lifemapper web service clients
@author: CJ Grady
@version: 3.3.4
@status: release

@license: Copyright (C) 2016, University of Kansas Center for Research

          Lifemapper Project, lifemapper [at] ku [dot] edu, 
          Biodiversity Institute,
          1345 Jayhawk Boulevard, Lawrence, Kansas, 66045, USA
   
          This program is free software; you can redistribute it and/or modify 
          it under the terms of the GNU General Public License as published by 
          the Free Software Foundation; either version 2 of the License, or (at 
          your option) any later version.
  
          This program is distributed in the hope that it will be useful, but 
          WITHOUT ANY WARRANTY; without even the implied warranty of 
          MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU 
          General Public License for more details.
  
          You should have received a copy of the GNU General Public License 
          along with this program; if not, write to the Free Software 
          Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 
          02110-1301, USA.
"""
CONTENT_TYPES = {
                 "AAIGrid" : "text/plain",
                 "GTiff" : "image/tiff"
                }

OTL_HINT_URL = "https://api.opentreeoflife.org/v2/tnrs/autocomplete_name"
OTL_TREE_WEB_URL = "https://api.opentreeoflife.org/v2/tree_of_life/subtree"
