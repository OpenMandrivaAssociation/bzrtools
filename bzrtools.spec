# spec originally for RHEL from: http://www.natemccallum.com/uploads/rpms/bzr/

Name:           bzrtools
Version:        0.90.0
Release:        %mkrel 1
Summary:        A collection of utilities and plugins for Bazaar-NG

Group:          Development/Other
License:        GPL
URL:            http://bazaar-vcs.org/BzrTools
Source0:        http://panoramicfeedback.com/opensource/%{name}-%{version}.tar.gz
Source1:        http://panoramicfeedback.com/opensource/%{name}-%{version}.tar.gz.sig
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(id -u -n)

BuildArch:      noarch
BuildRequires:  python-devel bzr
Requires:       python >= 2.4 bzr >= 0.18
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
python setup.py install --root $RPM_BUILD_ROOT --record=INSTALLED_FILES
# remove shebangs from all files as none should be executable scripts
sed -e '/^#!\//,1 d' -i $RPM_BUILD_ROOT/%py_puresitedir/bzrlib/plugins/bzrtools/*.py


%clean
rm -rf $RPM_BUILD_ROOT


%files -f INSTALLED_FILES
%defattr(-,root,root,-)
%doc README NEWS COPYING
