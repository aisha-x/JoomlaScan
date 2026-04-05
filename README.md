## Python3 Version of [Joomla Scanner](https://github.com/drego85/JoomlaScan)

Example: 
```bash
$ python3 joomlascan.py -u http://dev.inlanefreight.local 
-------------------------------------------
                Joomla Scan                  
    Usage: python3 joomlascan.py -u <target> 
     Version 0.5beta-py3 - Database Entries 1235
           created by Andrea Draghetti       
-------------------------------------------
Robots file found:               > http://dev.inlanefreight.local/robots.txt
No Error Log found

Start scan...with 10 concurrent threads!
Component found: com_actionlogs  > http://dev.inlanefreight.local/index.php?option=com_actionlogs
         On the administrator components
Component found: com_admin       > http://dev.inlanefreight.local/index.php?option=com_admin
         On the administrator components
Component found: com_ajax        > http://dev.inlanefreight.local/index.php?option=com_ajax
         But possibly it is not active or protected
         LICENSE file found      > http://dev.inlanefreight.local/administrator/components/com_actionlogs/actionlogs.xml
         LICENSE file found      > http://dev.inlanefreight.local/administrator/components/com_admin/admin.xml
         LICENSE file found      > http://dev.inlanefreight.local/administrator/components/com_ajax/ajax.xml
         Explorable Directory    > http://dev.inlanefreight.local/administrator/components/com_actionlogs/
         Explorable Directory    > http://dev.inlanefreight.local/administrator/components/com_admin/
Component found: com_banners     > http://dev.inlanefreight.local/index.php?option=com_banners
         But possibly it is not active or protected
         Explorable Directory    > http://dev.inlanefreight.local/components/com_ajax/
         Explorable Directory    > http://dev.inlanefreight.local/administrator/components/com_ajax/
         LICENSE file found      > http://dev.inlanefreight.local/administrator/components/com_banners/banners.xml
         Explorable Directory    > http://dev.inlanefreight.local/components/com_banners/
         Explorable Directory    > http://dev.inlanefreight.local/administrator/components/com_banners/
Component found: com_config      > http://dev.inlanefreight.local/index.php?option=com_config
Component found: com_contact     > http://dev.inlanefreight.local/index.php?option=com_contact
Component found: com_content     > http://dev.inlanefreight.local/index.php?option=com_content
Component found: com_contenthistory      > http://dev.inlanefreight.local/index.php?option=com_contenthistory
         But possibly it is not active or protected
         LICENSE file found      > http://dev.inlanefreight.local/administrator/components/com_config/config.xml
         LICENSE file found      > http://dev.inlanefreight.local/administrator/components/com_contact/contact.xml
         LICENSE file found      > http://dev.inlanefreight.local/administrator/components/com_content/content.xml
         LICENSE file found      > http://dev.inlanefreight.local/administrator/components/com_contenthistory/contenthistory.xml
         Explorable Directory    > http://dev.inlanefreight.local/components/com_contact/
         Explorable Directory    > http://dev.inlanefreight.local/components/com_config/
         Explorable Directory    > http://dev.inlanefreight.local/components/com_content/
         Explorable Directory    > http://dev.inlanefreight.local/administrator/components/com_contact/
         Explorable Directory    > http://dev.inlanefreight.local/administrator/components/com_config/
         Explorable Directory    > http://dev.inlanefreight.local/administrator/components/com_content/
         Explorable Directory    > http://dev.inlanefreight.local/components/com_contenthistory/
         Explorable Directory    > http://dev.inlanefreight.local/administrator/components/com_contenthistory/
Component found: com_fields      > http://dev.inlanefreight.local/index.php?option=com_fields
         But possibly it is not active or protected
         LICENSE file found      > http://dev.inlanefreight.local/administrator/components/com_fields/fields.xml
         Explorable Directory    > http://dev.inlanefreight.local/components/com_fields/
         Explorable Directory    > http://dev.inlanefreight.local/administrator/components/com_fields/
Component found: com_installer   > http://dev.inlanefreight.local/index.php?option=com_installer
         On the administrator components
         LICENSE file found      > http://dev.inlanefreight.local/administrator/components/com_installer/installer.xml
         Explorable Directory    > http://dev.inlanefreight.local/administrator/components/com_installer/
Component found: com_joomlaupdate        > http://dev.inlanefreight.local/index.php?option=com_joomlaupdate
         On the administrator components
         LICENSE file found      > http://dev.inlanefreight.local/administrator/components/com_joomlaupdate/joomlaupdate.xml
         Explorable Directory    > http://dev.inlanefreight.local/administrator/components/com_joomlaupdate/
Component found: com_mailto      > http://dev.inlanefreight.local/index.php?option=com_mailto
         But possibly it is not active or protected
Component found: com_media       > http://dev.inlanefreight.local/index.php?option=com_media
         But possibly it is not active or protected
         LICENSE file found      > http://dev.inlanefreight.local/components/com_mailto/mailto.xml
         LICENSE file found      > http://dev.inlanefreight.local/administrator/components/com_media/media.xml
         Explorable Directory    > http://dev.inlanefreight.local/components/com_mailto/
         Explorable Directory    > http://dev.inlanefreight.local/components/com_media/
Component found: com_newsfeeds   > http://dev.inlanefreight.local/index.php?option=com_newsfeeds
         Explorable Directory    > http://dev.inlanefreight.local/administrator/components/com_media/
         LICENSE file found      > http://dev.inlanefreight.local/administrator/components/com_newsfeeds/newsfeeds.xml
         Explorable Directory    > http://dev.inlanefreight.local/components/com_newsfeeds/
         Explorable Directory    > http://dev.inlanefreight.local/administrator/components/com_newsfeeds/
Component found: com_search      > http://dev.inlanefreight.local/index.php?option=com_search
         LICENSE file found      > http://dev.inlanefreight.local/administrator/components/com_search/search.xml
         Explorable Directory    > http://dev.inlanefreight.local/components/com_search/
         Explorable Directory    > http://dev.inlanefreight.local/administrator/components/com_search/
Component found: com_users       > http://dev.inlanefreight.local/index.php?option=com_users
         LICENSE file found      > http://dev.inlanefreight.local/administrator/components/com_users/users.xml
Component found: com_wrapper     > http://dev.inlanefreight.local/index.php?option=com_wrapper
         Explorable Directory    > http://dev.inlanefreight.local/components/com_users/
         Explorable Directory    > http://dev.inlanefreight.local/administrator/components/com_users/
         LICENSE file found      > http://dev.inlanefreight.local/components/com_wrapper/wrapper.xml
         Explorable Directory    > http://dev.inlanefreight.local/components/com_wrapper/
End Scanner

```
