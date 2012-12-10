# spec originally for RHEL from: http://www.natemccallum.com/uploads/rpms/bzr/

Name:		bzrtools
Version:	2.5
Release:	%mkrel 1
Summary:	A collection of utilities and plugins for Bazaar-NG
Group:		Development/Other
License:	GPLv2
URL:		http://bazaar-vcs.org/BzrTools
Source0:	https://launchpad.net/%{name}/stable/%{version}/+download/%{name}-%{version}.tar.gz
Source1:	https://launchpad.net/%{name}/stable/%{version}/+download/%{name}-%{version}.tar.gz.sig
BuildArch:	noarch
BuildRequires:	python-devel
BuildRequires:	bzr
Requires:	python
Requires:	bzr
Requires:	patch
Requires:	rsync
Requires:	graphviz
Requires:	librsvg
Requires:	python-paramiko

%description
BzrTools is a collection of plugins for Bazaar-NG (bzr).  Among the included
plugins are:
* push - uses rsync to push local changes to a remote server
* annotate - prints a file annotated with the revision next to each line
* baz-import - (Requres PyBaz) import an arch archive losslessly into bzr
* shelve/unshelve - allows you to undo some changes, commit, and restore
* clean-tree - remove unknown, ignored-junk, or unversioned files from the tree
* graph-ancestry - use dot to produce banch ancestry graphs
* shell - a bzr command interpreter with command completion
* patch - apply a patch to your tree from a file or URL


%prep
%setup -q -n %{name}

%build
CFLAGS="%{optflags}" python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root %{buildroot}
# remove shebangs from all files as none should be executable scripts
sed -e '/^#!\//,1 d' -i %{buildroot}%{py_puresitedir}/bzrlib/plugins/bzrtools/*.py

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README NEWS COPYING
%dir %{py_puresitedir}/bzrlib/plugins/bzrtools
%{py_puresitedir}/bzrlib/plugins/bzrtools/*.py
%dir %{py_puresitedir}/bzrlib/plugins/bzrtools/tests
%{py_puresitedir}/bzrlib/plugins/bzrtools/tests/*.py
%{py_puresitedir}/BzrTools*.egg-info


%changelog
* Wed Feb 08 2012 Andrey Bondrov <abondrov@mandriva.org> 2.5-1
+ Revision: 771824
- New version 2.5, minor spec cleanup

* Mon Nov 14 2011 Crispin Boylan <crisb@mandriva.org> 2.4.1-1
+ Revision: 730546
- New release

* Sat Aug 13 2011 Crispin Boylan <crisb@mandriva.org> 2.4.0-1
+ Revision: 694340
- New release

* Mon Feb 14 2011 Crispin Boylan <crisb@mandriva.org> 2.3.1-1
+ Revision: 637816
- New release

* Fri Oct 29 2010 Michael Scherer <misc@mandriva.org> 2.2.0-4mdv2011.0
+ Revision: 590151
- rebuild for python 2.7

* Tue Aug 31 2010 Ahmad Samir <ahmadsamir@mandriva.org> 2.2.0-3mdv2011.0
+ Revision: 574757
- drop pybaz, not needed any more (from misc)

* Sun Jun 27 2010 Crispin Boylan <crisb@mandriva.org> 2.2.0-2mdv2011.0
+ Revision: 549207
- New release

* Wed May 05 2010 Funda Wang <fwang@mandriva.org> 2.1.0-2mdv2010.1
+ Revision: 542315
- fix file list

* Wed Feb 17 2010 Crispin Boylan <crisb@mandriva.org> 2.1.0-1mdv2010.1
+ Revision: 506925
- New release

* Sun Sep 27 2009 Frederik Himpe <fhimpe@mandriva.org> 2.0.1-1mdv2010.0
+ Revision: 449727
- update to new version 2.0.1

* Tue Sep 15 2009 Crispin Boylan <crisb@mandriva.org> 2.0.0-1mdv2010.0
+ Revision: 442936
- New release

* Sun Aug 30 2009 Crispin Boylan <crisb@mandriva.org> 1.18.0-1mdv2010.0
+ Revision: 422404
- New release

* Tue Jul 21 2009 Frederik Himpe <fhimpe@mandriva.org> 1.17.0-1mdv2010.0
+ Revision: 398352
- Update to new version 1.17.0

* Thu Jun 18 2009 Frederik Himpe <fhimpe@mandriva.org> 1.16.0-1mdv2010.0
+ Revision: 387146
- update to new version 1.16.0

* Fri May 29 2009 Frederik Himpe <fhimpe@mandriva.org> 1.15.0-1mdv2010.0
+ Revision: 381159
- update to new version 1.15.0

* Wed Apr 29 2009 Crispin Boylan <crisb@mandriva.org> 1.14.0-1mdv2010.0
+ Revision: 369143
- New release

* Wed Mar 11 2009 Frederik Himpe <fhimpe@mandriva.org> 1.13.0-1mdv2009.1
+ Revision: 353963
- update to new version 1.13.0

* Wed Feb 11 2009 Frederik Himpe <fhimpe@mandriva.org> 1.12.0-1mdv2009.1
+ Revision: 339544
- update to new version 1.12.0

* Tue Jan 20 2009 Crispin Boylan <crisb@mandriva.org> 1.11.0-1mdv2009.1
+ Revision: 331723
- New binaries
- New release

* Sat Jan 10 2009 Crispin Boylan <crisb@mandriva.org> 1.10.0-3mdv2009.1
+ Revision: 328027
- Use proper file list

* Fri Dec 26 2008 Crispin Boylan <crisb@mandriva.org> 1.10.0-2mdv2009.1
+ Revision: 319421
- Rebuild for python2.6

* Sat Dec 06 2008 Crispin Boylan <crisb@mandriva.org> 1.10.0-1mdv2009.1
+ Revision: 310928
- New release

* Fri Nov 07 2008 Crispin Boylan <crisb@mandriva.org> 1.9.1-1mdv2009.1
+ Revision: 300440
- New version

* Sat Jun 14 2008 Jérôme Soyer <saispo@mandriva.org> 1.6.0-1mdv2009.0
+ Revision: 219149
- New release 1.6.0

* Wed May 14 2008 Bogdano Arendartchuk <bogdano@mandriva.com> 1.4.0-1mdv2009.0
+ Revision: 207322
- new version 1.4.0

* Mon Mar 03 2008 Bogdano Arendartchuk <bogdano@mandriva.com> 1.2.0-1mdv2008.1
+ Revision: 177977
- requires bzr >= 1.0
- new version 1.2.0

* Tue Jan 15 2008 Bogdano Arendartchuk <bogdano@mandriva.com> 1.1.0-1mdv2008.1
+ Revision: 152397
- new version 1.1.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Dec 14 2007 Jérôme Soyer <saispo@mandriva.org> 1.0.0-1mdv2008.1
+ Revision: 119743
- New release 1.0.0

* Fri Nov 09 2007 Jérôme Soyer <saispo@mandriva.org> 0.92.1-1mdv2008.1
+ Revision: 107069
- Delete
- Fix

* Fri Oct 12 2007 Jérôme Soyer <saispo@mandriva.org> 0.91.0-1mdv2008.1
+ Revision: 97326
- New release 0.91.0

* Mon Sep 03 2007 Bogdano Arendartchuk <bogdano@mandriva.com> 0.90.0-1mdv2008.0
+ Revision: 78570
- new version 0.90.0

* Tue Jul 17 2007 Bogdano Arendartchuk <bogdano@mandriva.com> 0.18.0-1mdv2008.0
+ Revision: 53029
- new version 0.18.0
- changed group to Development/Other

* Tue Jun 12 2007 Bogdano Arendartchuk <bogdano@mandriva.com> 0.17.0-1mdv2008.0
+ Revision: 38306
- updated to 0.17.0

* Mon May 28 2007 Bogdano Arendartchuk <bogdano@mandriva.com> 0.16.1-1mdv2008.0
+ Revision: 31927
- upgrade to 0.16.1
- ported package to Mandriva Linux
- Import bzrtools



* Wed May 24 2006 Shahms E. King <shahms@shahms.com> 0.8.1-4
- Require bzr >= 0.8, rather than only 0.8

* Tue May 16 2006 Shahms E. King <shahms@shahms.com> 0.8.1-3
- BuildRequires python, rather than python-devel

* Mon May 15 2006 Shahms E. King <shahms@shahms.com> 0.8.1-2
- Fix rpmlint non-executable-script errors

* Fri May 12 2006 Shahms E. King <shahms@shahms.com> 0.8.1-1
- Add COPYING to %%doc
- Update to new upstream version
- Require bzr 0.8

* Wed May 10 2006 Shahms E. King <shahms@shahms.com> 0.8-1
- Update to new upstream version

* Fri Apr 14 2006 Shahms E. King <shahms@shahms.com> 0.7-1
- Initial package
