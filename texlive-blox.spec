%global tl_name blox
%global tl_revision 57949

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.51
Release:	%{tl_revision}.1
Summary:	Draw block diagrams, using TikZ
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/blox
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/blox.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/blox.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/blox.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package, along with TikZ, will typeset block diagrams for use with
programming and control theory. It is an English translation of the
schemabloc package.

