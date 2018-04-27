#include <nds.h>

void fifocheck (void)
{
	if(fifoCheckValue32(FIFO_USER_04)) {
		if(fifoCheckValue32(FIFO_USER_03)) {
			i2cWriteRegister(0x4A, 0x70, 0x00);	// Bootflag = Softboot
		} else {
			i2cWriteRegister(0x4A, 0x70, 0x01);	// Bootflag = Warmboot/SkipHealthSafety
		}
		// After writing i2c, set FIFO_USER_04 back to 0 so arm7 doesn't repeatedly run i2c code.
		fifoSendValue32(FIFO_USER_04, 0);
	}
}

