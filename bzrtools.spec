%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           bzrtools
Version:        0.8.1
Release:        4%{?dist}
Summary:        A collection of utilities and plugins for Bazaar-NG

Group:          Development/Tools
License:        GPL
URL:            http://bazaar-vcs.org/BzrTools
Source0:        http://panoramicfeedback.com/opensource/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python24
Requires:   python-abi = %(%{__python} -c "import sys ; print sys.version[:3]")
Requires:   bzr >= 0.8

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
%setup -q


%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
# remove shebangs from all files as none should be executable scripts
sed -e '/^#!\//,1 d' -i $RPM_BUILD_ROOT/%{python_sitelib}/bzrlib/plugins/bzrtools/*.py


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README NEWS COPYING
%dir %{python_sitelib}/bzrlib/plugins/bzrtools
%{python_sitelib}/bzrlib/plugins/bzrtools/*.py
%{python_sitelib}/bzrlib/plugins/bzrtools/*.pyc
%ghost %{python_sitelib}/bzrlib/plugins/bzrtools/*.pyo
