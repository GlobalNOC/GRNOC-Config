#!/usr/bin/perl
use strict;
use warnings;
use ExtUtils::MakeMaker;

sub MY::postamble { <<"END"; }
venv:
	carton install --deployment --path=venv

rpm:  manifest dist
	rpmbuild -ta GRNOC-Config-\$(VERSION).tar.gz

END

WriteMakefile(
    NAME                => 'GRNOC::Config',
    AUTHOR              => 'GRNOC Systems Engineering <syseng@grnoc.iu.edu>',
    VERSION_FROM        => 'lib/GRNOC/Config.pm',
    ABSTRACT_FROM       => 'lib/GRNOC/Config.pm',
	      PL_FILES            => {},
	      PREREQ_PM => {
		  'Test::More'=> 0,
		  'XML::Simple'=> 0,
		  'XML::XPath' => 0,
		  'XML::LibXML' => 0,
	      },
	      dist                => { COMPRESS => 'gzip -9f', SUFFIX => 'gz', },
	      clean               => { FILES => 'GRNOC-Config-* venv' },
	      );

sub MY::test
{
    q(
TEST_VERBOSE=1

test : pure_all
	$(FULLPERL) t/TEST $(TEST_VERBOSE)

test_jenkins : pure_all
	$(FULLPERL) t/TEST $(TEST_VERBOSE) --formatter=TAP::Formatter::Console

    );
}
