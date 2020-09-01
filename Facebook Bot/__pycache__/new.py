ht, last_ht = 0,1
		while ht != last_ht:
			last_ht = ht
			sleep(1)
			ht = self.driver.execute_script("""
				arguments[0].scrollTo(0,arguments[0].scrollHeight);
				return arguments[0].scrollHeight;
				""", scroll_box)