include ../config.h

install:
	$(PYTHON) setup.py install --prefix=$(AMBERHOME) --install-scripts=$(BINDIR)

clean:
	/bin/rm -rf build/

uninstall:
	/bin/rm -f $(BINDIR)/MCPB.py $(BINDIR)/OptC4.py $(BINDIR)/PdbSearcher.py $(BINDIR)/IPMach.py $(BINDIR)/CartHess2FC.py $(BINDIR)/espgen.py

skip:
	@echo ""
	@echo "Skipping installation of pyMSMT."
	@echo ""

