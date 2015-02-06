# spec originally for RHEL from: http://www.natemccallum.com/uploads/rpms/bzr/

Name:		bzrtools
Version:	2.6.0
Release:	2
Summary:	A collection of utilities and plugins for Bazaar-NG
Group:		Development/Other
License:	GPLv2
URL:		http://bazaar-vcs.org/BzrTools
Source0:	https://launchpad.net/%{name}/stable/%{version}/+download/%{name}-%{version}.tar.gz
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
python setup.py install --root %{buildroot}
# remove shebangs from all files as none should be executable scripts
sed -e '/^#!\//,1 d' -i %{buildroot}%{py_puresitedir}/bzrlib/plugins/bzrtools/*.py

%files
%doc README NEWS COPYING
%dir %{py_puresitedir}/bzrlib/plugins/bzrtools
%{py_puresitedir}/bzrlib/plugins/bzrtools/*.py
%dir %{py_puresitedir}/bzrlib/plugins/bzrtools/tests
%{py_puresitedir}/bzrlib/plugins/bzrtools/tests/*.py
%{py_puresitedir}/BzrTools*.egg-info

