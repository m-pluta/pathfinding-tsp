SCRIPT = AlgAenhanced_AWA.py

clean:
	rm *.txt

prof:
	kernprof -lv $(SCRIPT) > out.prof
	rm $(SCRIPT).lprof
	make clean