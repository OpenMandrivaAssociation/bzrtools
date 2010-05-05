# spec originally for RHEL from: http://www.natemccallum.com/uploads/rpms/bzr/

Name:           bzrtools
Version:        2.1.0
Release:        %mkrel 2
Summary:        A collection of utilities and plugins for Bazaar-NG

Group:          Development/Other
License:        GPL
URL:            http://bazaar-vcs.org/BzrTools
Source0:        https://launchpad.net/%{name}/stable/%{version}/+download/%{name}-%{version}.tar.gz
Source1:        https://launchpad.net/%{name}/stable/%{version}/+download/%{name}-%{version}.tar.gz.sig
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(id -u -n)

BuildArch:      noarch
BuildRequires:  python-devel bzr
Requires:       python >= 2.4
Requires:       bzr >= 2.0
Requires:       patch >= 2.5.9 rsync graphviz librsvg python-paramiko
Requires:       python-pybaz

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
CFLAGS="$RPM_OPT_FLAGS" python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root $RPM_BUILD_ROOT 
# remove shebangs from all files as none should be executable scripts
sed -e '/^#!\//,1 d' -i $RPM_BUILD_ROOT/%py_puresitedir/bzrlib/plugins/bzrtools/*.py


%clean
rm -rf $RPM_BUILD_ROOT


%files 
%defattr(-,root,root,-)
%dir %py_puresitedir/bzrlib/plugins/bzrtools
%py_puresitedir/bzrlib/plugins/bzrtools/*.py
%dir %py_puresitedir/bzrlib/plugins/bzrtools/tests
%py_puresitedir/bzrlib/plugins/bzrtools/tests/*.py
%py_puresitedir/BzrTools*.egg-info
%doc README NEWS COPYING
