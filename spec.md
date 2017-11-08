worker 1
```bash
cudal                       
    description: Desktop Computer
    product: To be filled by O.E.M. (To be filled by O.E.M.)
    vendor: Gigabyte Technology Co., Ltd.
    version: To be filled by O.E.M.
    serial: To be filled by O.E.M.
    width: 64 bits
    capabilities: smbios-2.7 dmi-2.7 smp vsyscall32
    configuration: boot=normal chassis=desktop family=To be filled by O.E.M. sku=To be filled by O.E.M. uuid=5002E503-4904-EC05-7906-1B0700080009
  *-core
       description: Motherboard
       product: Z77X-D3H
       vendor: Gigabyte Technology Co., Ltd.
       physical id: 0
       version: x.x
       serial: To be filled by O.E.M.
       slot: To be filled by O.E.M.
     *-firmware
          description: BIOS
          vendor: American Megatrends Inc.
          physical id: 0
          version: F16
          date: 10/24/2012
          size: 64KiB
          capacity: 8128KiB
          capabilities: pci upgrade shadowing cdboot bootselect socketedrom edd int13floppy1200 int13floppy720 int13floppy2880 int5printscreen int9keyboard int14serial int17printer acpi usb biosbootspecification uefi
     *-cache:0
          description: L1 cache
          physical id: 4
          slot: CPU Internal L1
          size: 128KiB
          capacity: 128KiB
          capabilities: internal write-through
          configuration: level=1
     *-cache:1
          description: L2 cache
          physical id: 5
          slot: CPU Internal L2
          size: 1MiB
          capacity: 1MiB
          capabilities: internal write-through instruction
          configuration: level=2
     *-cache:2
          description: L3 cache
          physical id: 6
          slot: CPU Internal L3
          size: 6MiB
          capacity: 6MiB
          capabilities: internal write-back instruction
          configuration: level=3
     *-memory
          description: System Memory
          physical id: 7
          slot: System board or motherboard
          size: 24GiB
        *-bank:0
             description: DIMM DDR3 Synchronous 1333 MHz (0.8 ns)
             product: KHX1600C10D3/8G
             vendor: Kingston
             physical id: 0
             serial: 2003CD67
             slot: ChannelA-DIMM0
             size: 8GiB
             width: 64 bits
             clock: 1333MHz (0.8ns)
        *-bank:1
             description: DIMM DDR3 Synchronous 1333 MHz (0.8 ns)
             product: 9905403-439.A00LF
             vendor: Kingston
             physical id: 1
             serial: 8B35D911
             slot: ChannelA-DIMM1
             size: 4GiB
             width: 64 bits
             clock: 1333MHz (0.8ns)
        *-bank:2
             description: DIMM DDR3 Synchronous 1333 MHz (0.8 ns)
             product: KHX1600C10D3/8G
             vendor: Kingston
             physical id: 2
             serial: 21034768
             slot: ChannelB-DIMM0
             size: 8GiB
             width: 64 bits
             clock: 1333MHz (0.8ns)
        *-bank:3
             description: DIMM DDR3 Synchronous 1333 MHz (0.8 ns)
             product: 9905403-439.A00LF
             vendor: Kingston
             physical id: 3
             serial: 8C35DE11
             slot: ChannelB-DIMM1
             size: 4GiB
             width: 64 bits
             clock: 1333MHz (0.8ns)
     *-cpu
          description: CPU
          product: Intel(R) Core(TM) i5-2400 CPU @ 3.10GHz
          vendor: Intel Corp.
          vendor_id: GenuineIntel
          physical id: 43
          bus info: cpu@0
          version: Intel(R) Core(TM) i5-2400 CPU @ 3.10GHz
          slot: Intel(R) Core(TM) i5-2400 CPU @ 3.10GHz
          size: 3199MHz
          capacity: 3400MHz
          width: 64 bits
          clock: 100MHz
          capabilities: lm fpu fpu_exception wp vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx rdtscp x86-64 constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic popcnt tsc_deadline_timer aes xsave avx lahf_lm epb tpr_shadow vnmi flexpriority ept vpid xsaveopt dtherm ida arat pln pts cpufreq
          configuration: cores=4 enabledcores=1
     *-pci
          description: Host bridge
          product: 2nd Generation Core Processor Family DRAM Controller
          vendor: Intel Corporation
          physical id: 100
          bus info: pci@0000:00:00.0
          version: 09
          width: 32 bits
          clock: 33MHz
          configuration: driver=snb_uncore
          resources: irq:0
        *-pci:0
             description: PCI bridge
             product: Xeon E3-1200/2nd Generation Core Processor Family PCI Express Root Port
             vendor: Intel Corporation
             physical id: 1
             bus info: pci@0000:00:01.0
             version: 09
             width: 32 bits
             clock: 33MHz
             capabilities: pci pm msi pciexpress normal_decode bus_master cap_list
             configuration: driver=pcieport
             resources: irq:26 memory:f6000000-f6ffffff ioport:e0000000(size=301989888)
           *-display
                description: 3D controller
                product: GK110BGL [Tesla K40c]
                vendor: NVIDIA Corporation
                physical id: 0
                bus info: pci@0000:01:00.0
                version: a1
                width: 64 bits
                clock: 33MHz
                capabilities: pm msi pciexpress bus_master cap_list
                configuration: driver=nvidia latency=0
                resources: irq:35 memory:f6000000-f6ffffff memory:e0000000-efffffff memory:f0000000-f1ffffff
        *-display
             description: VGA compatible controller
             product: 2nd Generation Core Processor Family Integrated Graphics Controller
             vendor: Intel Corporation
             physical id: 2
             bus info: pci@0000:00:02.0
             version: 09
             width: 64 bits
             clock: 33MHz
             capabilities: msi pm vga_controller bus_master cap_list rom
             configuration: driver=i915 latency=0
             resources: irq:31 memory:f7000000-f73fffff memory:d0000000-dfffffff ioport:f000(size=64)
        *-usb:0
             description: USB controller
             product: 7 Series/C210 Series Chipset Family USB xHCI Host Controller
             vendor: Intel Corporation
             physical id: 14
             bus info: pci@0000:00:14.0
             version: 04
             width: 64 bits
             clock: 33MHz
             capabilities: pm msi xhci bus_master cap_list
             configuration: driver=xhci_hcd latency=0
             resources: irq:27 memory:f7700000-f770ffff
           *-usbhost:0
                product: xHCI Host Controller
                vendor: Linux 3.10.0-693.5.2.el7.x86_64 xhci-hcd
                physical id: 0
                bus info: usb@3
                logical name: usb3
                version: 3.10
                capabilities: usb-2.00
                configuration: driver=hub slots=4 speed=480Mbit/s
           *-usbhost:1
                product: xHCI Host Controller
                vendor: Linux 3.10.0-693.5.2.el7.x86_64 xhci-hcd
                physical id: 1
                bus info: usb@4
                logical name: usb4
                version: 3.10
                capabilities: usb-3.00
                configuration: driver=hub slots=4 speed=5000Mbit/s
        *-communication
             description: Communication controller
             product: 7 Series/C216 Chipset Family MEI Controller #1
             vendor: Intel Corporation
             physical id: 16
             bus info: pci@0000:00:16.0
             version: 04
             width: 64 bits
             clock: 33MHz
             capabilities: pm msi bus_master cap_list
             configuration: driver=mei_me latency=0
             resources: irq:32 memory:f771a000-f771a00f
        *-usb:1
             description: USB controller
             product: 7 Series/C216 Chipset Family USB Enhanced Host Controller #2
             vendor: Intel Corporation
             physical id: 1a
             bus info: pci@0000:00:1a.0
             version: 04
             width: 32 bits
             clock: 33MHz
             capabilities: pm debug ehci bus_master cap_list
             configuration: driver=ehci-pci latency=0
             resources: irq:16 memory:f7718000-f77183ff
           *-usbhost
                product: EHCI Host Controller
                vendor: Linux 3.10.0-693.5.2.el7.x86_64 ehci_hcd
                physical id: 1
                bus info: usb@1
                logical name: usb1
                version: 3.10
                capabilities: usb-2.00
                configuration: driver=hub slots=2 speed=480Mbit/s
              *-usb
                   description: USB hub
                   product: Integrated Rate Matching Hub
                   vendor: Intel Corp.
                   physical id: 1
                   bus info: usb@1:1
                   version: 0.00
                   capabilities: usb-2.00
                   configuration: driver=hub slots=6 speed=480Mbit/s
        *-multimedia
             description: Audio device
             product: 7 Series/C216 Chipset Family High Definition Audio Controller
             vendor: Intel Corporation
             physical id: 1b
             bus info: pci@0000:00:1b.0
             version: 04
             width: 64 bits
             clock: 33MHz
             capabilities: pm msi pciexpress bus_master cap_list
             configuration: driver=snd_hda_intel latency=0
             resources: irq:33 memory:f7710000-f7713fff
        *-pci:1
             description: PCI bridge
             product: 7 Series/C216 Chipset Family PCI Express Root Port 1
             vendor: Intel Corporation
             physical id: 1c
             bus info: pci@0000:00:1c.0
             version: c4
             width: 32 bits
             clock: 33MHz
             capabilities: pci pciexpress msi pm normal_decode bus_master cap_list
             configuration: driver=pcieport
             resources: irq:16
        *-pci:2
             description: PCI bridge
             product: 7 Series/C210 Series Chipset Family PCI Express Root Port 5
             vendor: Intel Corporation
             physical id: 1c.4
             bus info: pci@0000:00:1c.4
             version: c4
             width: 32 bits
             clock: 33MHz
             capabilities: pci pciexpress msi pm normal_decode bus_master cap_list
             configuration: driver=pcieport
             resources: irq:16 memory:f7600000-f76fffff
           *-usb
                description: USB controller
                product: VL80x xHCI USB 3.0 Controller
                vendor: VIA Technologies, Inc.
                physical id: 0
                bus info: pci@0000:03:00.0
                version: 03
                width: 32 bits
                clock: 33MHz
                capabilities: pm msi pciexpress xhci bus_master cap_list
                configuration: driver=xhci_hcd latency=0
                resources: irq:28 memory:f7600000-f7600fff
              *-usbhost:0
                   product: xHCI Host Controller
                   vendor: Linux 3.10.0-693.5.2.el7.x86_64 xhci-hcd
                   physical id: 0
                   bus info: usb@5
                   logical name: usb5
                   version: 3.10
                   capabilities: usb-2.00
                   configuration: driver=hub slots=1 speed=480Mbit/s
                 *-usb
                      description: USB hub
                      product: USB2.0 Hub
                      vendor: VIA Labs, Inc.
                      physical id: 1
                      bus info: usb@5:1
                      version: 2.00
                      capabilities: usb-2.00
                      configuration: driver=hub maxpower=100mA slots=4 speed=480Mbit/s
              *-usbhost:1
                   product: xHCI Host Controller
                   vendor: Linux 3.10.0-693.5.2.el7.x86_64 xhci-hcd
                   physical id: 1
                   bus info: usb@6
                   logical name: usb6
                   version: 3.10
                   capabilities: usb-3.00
                   configuration: driver=hub slots=4 speed=5000Mbit/s
        *-pci:3
             description: PCI bridge
             product: 82801 PCI Bridge
             vendor: Intel Corporation
             physical id: 1c.5
             bus info: pci@0000:00:1c.5
             version: c4
             width: 32 bits
             clock: 33MHz
             capabilities: pci pciexpress msi pm subtractive_decode bus_master cap_list
           *-pci
                description: PCI bridge
                product: 82801 PCI Bridge
                vendor: Intel Corporation
                physical id: 0
                bus info: pci@0000:04:00.0
                version: 30
                width: 64 bits
                clock: 33MHz
                capabilities: pci pm subtractive_decode bus_master cap_list
                resources: iomemory:222001f10-222001f0f
        *-pci:4
             description: PCI bridge
             product: 7 Series/C210 Series Chipset Family PCI Express Root Port 7
             vendor: Intel Corporation
             physical id: 1c.6
             bus info: pci@0000:00:1c.6
             version: c4
             width: 32 bits
             clock: 33MHz
             capabilities: pci pciexpress msi pm normal_decode bus_master cap_list
             configuration: driver=pcieport
             resources: irq:18 ioport:e000(size=4096) memory:f7500000-f75fffff
           *-network
                description: Ethernet interface
                product: AR8151 v2.0 Gigabit Ethernet
                vendor: Qualcomm Atheros
                physical id: 0
                bus info: pci@0000:06:00.0
                logical name: enp6s0
                version: c0
                serial: 50:e5:49:ec:79:1b
                size: 1Gbit/s
                capacity: 1Gbit/s
                width: 64 bits
                clock: 33MHz
                capabilities: pm msi pciexpress vpd bus_master cap_list ethernet physical tp 10bt 10bt-fd 100bt 100bt-fd 1000bt-fd autonegotiation
                configuration: autonegotiation=on broadcast=yes driver=atl1c driverversion=1.0.1.1-NAPI duplex=full ip=158.108.38.91 latency=0 link=yes multicast=yes port=twisted pair speed=1Gbit/s
                resources: irq:34 memory:f7500000-f753ffff ioport:e000(size=128)
        *-pci:5
             description: PCI bridge
             product: 7 Series/C210 Series Chipset Family PCI Express Root Port 8
             vendor: Intel Corporation
             physical id: 1c.7
             bus info: pci@0000:00:1c.7
             version: c4
             width: 32 bits
             clock: 33MHz
             capabilities: pci pciexpress msi pm normal_decode bus_master cap_list
             configuration: driver=pcieport
             resources: irq:19 ioport:d000(size=4096) memory:f7400000-f74fffff
           *-sata
                description: SATA controller
                product: 88SE9172 SATA 6Gb/s Controller
                vendor: Marvell Technology Group Ltd.
                physical id: 0
                bus info: pci@0000:07:00.0
                version: 11
                width: 32 bits
                clock: 33MHz
                capabilities: sata pm msi pciexpress ahci_1.0 bus_master cap_list rom
                configuration: driver=ahci latency=0
                resources: irq:30 ioport:d040(size=8) ioport:d030(size=4) ioport:d020(size=8) ioport:d010(size=4) ioport:d000(size=16) memory:f7410000-f74101ff memory:f7400000-f740ffff
        *-usb:2
             description: USB controller
             product: 7 Series/C216 Chipset Family USB Enhanced Host Controller #1
             vendor: Intel Corporation
             physical id: 1d
             bus info: pci@0000:00:1d.0
             version: 04
             width: 32 bits
             clock: 33MHz
             capabilities: pm debug ehci bus_master cap_list
             configuration: driver=ehci-pci latency=0
             resources: irq:23 memory:f7717000-f77173ff
           *-usbhost
                product: EHCI Host Controller
                vendor: Linux 3.10.0-693.5.2.el7.x86_64 ehci_hcd
                physical id: 1
                bus info: usb@2
                logical name: usb2
                version: 3.10
                capabilities: usb-2.00
                configuration: driver=hub slots=2 speed=480Mbit/s
              *-usb
                   description: USB hub
                   product: Integrated Rate Matching Hub
                   vendor: Intel Corp.
                   physical id: 1
                   bus info: usb@2:1
                   version: 0.00
                   capabilities: usb-2.00
                   configuration: driver=hub slots=8 speed=480Mbit/s
        *-isa
             description: ISA bridge
             product: Z77 Express Chipset LPC Controller
             vendor: Intel Corporation
             physical id: 1f
             bus info: pci@0000:00:1f.0
             version: 04
             width: 32 bits
             clock: 33MHz
             capabilities: isa bus_master cap_list
             configuration: driver=lpc_ich latency=0
             resources: irq:0
        *-sata
             description: SATA controller
             product: 7 Series/C210 Series Chipset Family 6-port SATA Controller [AHCI mode]
             vendor: Intel Corporation
             physical id: 1f.2
             bus info: pci@0000:00:1f.2
             logical name: scsi0
             version: 04
             width: 32 bits
             clock: 66MHz
             capabilities: sata msi pm ahci_1.0 bus_master cap_list emulated
             configuration: driver=ahci latency=0
             resources: irq:29 ioport:f0b0(size=8) ioport:f0a0(size=4) ioport:f090(size=8) ioport:f080(size=4) ioport:f060(size=32) memory:f7716000-f77167ff
           *-disk
                description: ATA Disk
                product: TOSHIBA MD04ACA5
                vendor: Toshiba
                physical id: 0.0.0
                bus info: scsi@0:0.0.0
                logical name: /dev/sda
                version: FP2A
                serial: 36A4K9KVFS9A
                size: 4657GiB (5TB)
                capabilities: gpt-1.00 partitioned partitioned:gpt
                configuration: ansiversion=5 guid=b4ea10fc-96ca-4a8f-ad25-59b92cc95ef9 logicalsectorsize=512 sectorsize=4096
              *-volume:0
                   description: Windows FAT volume
                   vendor: mkfs.fat
                   physical id: 1
                   bus info: scsi@0:0.0.0,1
                   logical name: /dev/sda1
                   logical name: /boot/efi
                   version: FAT16
                   serial: bda9-4cd7
                   size: 199MiB
                   capacity: 199MiB
                   capabilities: boot fat initialized
                   configuration: FATs=2 filesystem=fat mount.fstype=vfat mount.options=rw,relatime,fmask=0077,dmask=0077,codepage=437,iocharset=ascii,shortname=winnt,errors=remount-ro name=EFI System Partition state=mounted
              *-volume:1
                   description: data partition
                   vendor: Windows
                   physical id: 2
                   bus info: scsi@0:0.0.0,2
                   logical name: /dev/sda2
                   logical name: /boot
                   serial: 49c6c008-fc86-4eaa-a216-05e62c2da650
                   capacity: 499MiB
                   configuration: mount.fstype=xfs mount.options=rw,seclabel,relatime,attr2,inode64,noquota state=mounted
              *-volume:2
                   description: LVM Physical Volume
                   vendor: Linux
                   physical id: 3
                   bus info: scsi@0:0.0.0,3
                   logical name: /dev/sda3
                   serial: zSwjDx-Qeh3-wNiI-ctEI-N38B-iD5Z-5SYk8U
                   size: 4656GiB
                   capabilities: multi lvm2
        *-serial UNCLAIMED
             description: SMBus
             product: 7 Series/C216 Chipset Family SMBus Controller
             vendor: Intel Corporation
             physical id: 1f.3
             bus info: pci@0000:00:1f.3
             version: 04
             width: 64 bits
             clock: 33MHz
             configuration: latency=0
             resources: memory:f7715000-f77150ff ioport:f040(size=32)
     *-pnp00:00
          product: PnP device PNP0c01
          physical id: 1
          capabilities: pnp
          configuration: driver=system
     *-pnp00:01
          product: PnP device PNP0c02
          physical id: 2
          capabilities: pnp
          configuration: driver=system
     *-pnp00:02
          product: PnP device PNP0b00
          physical id: 3
          capabilities: pnp
          configuration: driver=rtc_cmos
     *-pnp00:03
          product: PnP device INT3f0d
          vendor: Interphase Corporation
          physical id: 8
          capabilities: pnp
          configuration: driver=system
     *-pnp00:04
          product: PnP device PNP0c02
          physical id: 9
          capabilities: pnp
          configuration: driver=system
     *-pnp00:05
          product: PnP device PNP0501
          physical id: a
          capabilities: pnp
          configuration: driver=serial
     *-pnp00:06
          product: PnP device PNP0c02
          physical id: b
          capabilities: pnp
          configuration: driver=system
     *-pnp00:07
          product: PnP device PNP0c02
          physical id: c
          capabilities: pnp
          configuration: driver=system
     *-pnp00:08
          product: PnP device PNP0c01
          physical id: d
          capabilities: pnp
          configuration: driver=system
  *-power UNCLAIMED
       description: To Be Filled By O.E.M.
       product: To Be Filled By O.E.M.
       vendor: To Be Filled By O.E.M.
       physical id: 1
       version: To Be Filled By O.E.M.
       serial: To Be Filled By O.E.M.
       capacity: 32768mWh
  *-network:0
       description: Ethernet interface
       physical id: 2
       logical name: veth7c3ef35
       serial: b6:3c:5d:c8:14:6e
       size: 10Gbit/s
       capabilities: ethernet physical
       configuration: autonegotiation=off broadcast=yes driver=veth driverversion=1.0 duplex=full link=yes multicast=yes port=twisted pair speed=10Gbit/s
  *-network:1
       description: Ethernet interface
       physical id: 3
       logical name: vethff5d318
       serial: 16:4b:43:18:a5:28
       size: 10Gbit/s
       capabilities: ethernet physical
       configuration: autonegotiation=off broadcast=yes driver=veth driverversion=1.0 duplex=full link=yes multicast=yes port=twisted pair speed=10Gbit/s
  *-network:2
       description: Ethernet interface
       physical id: 4
       logical name: veth602fd64
       serial: e6:0f:c7:c6:7d:6b
       size: 10Gbit/s
       capabilities: ethernet physical
       configuration: autonegotiation=off broadcast=yes driver=veth driverversion=1.0 duplex=full link=yes multicast=yes port=twisted pair speed=10Gbit/s
  *-network:3
       description: Ethernet interface
       physical id: 5
       logical name: veth5373a86
       serial: f2:16:4c:f8:58:17
       size: 10Gbit/s
       capabilities: ethernet physical
       configuration: autonegotiation=off broadcast=yes driver=veth driverversion=1.0 duplex=full link=yes multicast=yes port=twisted pair speed=10Gbit/s
  *-network:4
       description: Ethernet interface
       physical id: 6
       logical name: veth9ee97f1
       serial: 62:4f:87:00:aa:b4
       size: 10Gbit/s
       capabilities: ethernet physical
       configuration: autonegotiation=off broadcast=yes driver=veth driverversion=1.0 duplex=full link=yes multicast=yes port=twisted pair speed=10Gbit/s
  *-network:5 DISABLED
       description: Ethernet interface
       physical id: 7
       logical name: virbr0-nic
       serial: 52:54:00:86:a4:cb
       size: 10Mbit/s
       capabilities: ethernet physical
       configuration: autonegotiation=off broadcast=yes driver=tun driverversion=1.6 duplex=full link=no multicast=yes port=twisted pair speed=10Mbit/s
  *-network:6
       description: Ethernet interface
       physical id: 8
       logical name: virbr0
       serial: 52:54:00:86:a4:cb
       capabilities: ethernet physical
       configuration: broadcast=yes driver=bridge driverversion=2.3 firmware=N/A ip=192.168.122.1 link=no multicast=yes
  *-network:7
       description: Ethernet interface
       physical id: 9
       logical name: veth1f1dc8e
       serial: 7a:bd:da:ce:f2:0a
       size: 10Gbit/s
       capabilities: ethernet physical
       configuration: autonegotiation=off broadcast=yes driver=veth driverversion=1.0 duplex=full link=yes multicast=yes port=twisted pair speed=10Gbit/s
  *-network:8
       description: Ethernet interface
       physical id: a
       logical name: veth3531841
       serial: 4a:32:3b:2f:89:a2
       size: 10Gbit/s
       capabilities: ethernet physical
       configuration: autonegotiation=off broadcast=yes driver=veth driverversion=1.0 duplex=full link=yes multicast=yes port=twisted pair speed=10Gbit/s
  *-network:9
       description: Ethernet interface
       physical id: b
       logical name: docker_gwbridge
       serial: 02:42:3f:ca:fb:14
       capabilities: ethernet physical
       configuration: broadcast=yes driver=bridge driverversion=2.3 firmware=N/A ip=172.18.0.1 link=yes multicast=yes
  *-network:10
       description: Ethernet interface
       physical id: c
       logical name: docker0
       serial: 02:42:6c:b6:bf:5d
       capabilities: ethernet physical
       configuration: broadcast=yes driver=bridge driverversion=2.3 firmware=N/A ip=172.17.0.1 link=yes multicast=yes
```

worker 2

```bash
tx1host                     
    description: Desktop Computer
    product: EX58-UD3R
    vendor: Gigabyte Technology Co., Ltd.
    width: 64 bits
    capabilities: smbios-2.4 dmi-2.4 smp vsyscall32
    configuration: boot=normal chassis=desktop uuid=00000000-0000-0000-0000-00241DC0B595
  *-core
       description: Motherboard
       product: EX58-UD3R
       vendor: Gigabyte Technology Co., Ltd.
       physical id: 0
       version: x.x
     *-firmware
          description: BIOS
          vendor: Award Software International, Inc.
          physical id: 0
          version: FB
          date: 05/04/2009
          size: 128KiB
          capacity: 1984KiB
          capabilities: pci pnp upgrade shadowing cdboot bootselect edd int13floppy360 int13floppy1200 int13floppy720 int13floppy2880 int5printscreen int9keyboard int14serial int17printer int10video acpi usb ls120boot zipboot biosbootspecification
     *-cpu
          description: CPU
          product: Intel(R) Core(TM) i7 CPU         920  @ 2.67GHz
          vendor: Intel Corp.
          physical id: 4
          bus info: cpu@0
          version: Intel(R) Core(TM) i7 CPU
          slot: Socket 1366
          size: 1596MHz
          capacity: 4GHz
          width: 64 bits
          clock: 133MHz
          capabilities: fpu fpu_exception wp vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx rdtscp x86-64 constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf pni dtes64 monitor ds_cpl vmx est tm2 ssse3 cx16 xtpr pdcm sse4_1 sse4_2 popcnt lahf_lm tpr_shadow vnmi flexpriority ept vpid dtherm ida cpufreq
        *-cache:0
             description: L1 cache
             physical id: a
             slot: Internal Cache
             size: 64KiB
             capacity: 64KiB
             capabilities: synchronous internal write-back
             configuration: level=1
        *-cache:1
             description: L2 cache
             physical id: b
             slot: External Cache
             size: 8MiB
             capabilities: synchronous internal write-back
             configuration: level=2
     *-memory
          description: System Memory
          physical id: 16
          slot: System board or motherboard
          size: 16GiB
        *-bank:0
             description: DIMM 800 MHz (1.2 ns)
             physical id: 0
             slot: A0
             size: 4GiB
             width: 4 bits
             clock: 800MHz (1.2ns)
        *-bank:1
             description: DIMM 800 MHz (1.2 ns)
             physical id: 1
             slot: A1
             size: 8GiB
             width: 2052 bits
             clock: 800MHz (1.2ns)
        *-bank:2
             description: DIMM 800 MHz (1.2 ns)
             physical id: 2
             slot: A2
             size: 4GiB
             width: 4 bits
             clock: 800MHz (1.2ns)
        *-bank:3
             description: DIMM [empty]
             physical id: 3
             slot: A3
     *-pci:0
          description: Host bridge
          product: 5520/5500/X58 I/O Hub to ESI Port
          vendor: Intel Corporation
          physical id: 100
          bus info: pci@0000:00:00.0
          version: 13
          width: 32 bits
          clock: 33MHz
        *-pci:0
             description: PCI bridge
             product: 5520/5500/X58 I/O Hub PCI Express Root Port 1
             vendor: Intel Corporation
             physical id: 1
             bus info: pci@0000:00:01.0
             version: 13
             width: 32 bits
             clock: 33MHz
             capabilities: pci msi pciexpress pm normal_decode cap_list
             configuration: driver=pcieport
             resources: irq:16
        *-pci:1
             description: PCI bridge
             product: 5520/5500/X58 I/O Hub PCI Express Root Port 3
             vendor: Intel Corporation
             physical id: 3
             bus info: pci@0000:00:03.0
             version: 13
             width: 32 bits
             clock: 33MHz
             capabilities: pci msi pciexpress pm normal_decode bus_master cap_list
             configuration: driver=pcieport
             resources: irq:16 ioport:e000(size=4096) memory:f9000000-faffffff ioport:b0000000(size=536870912)
           *-display
                description: VGA compatible controller
                product: GM204 [GeForce GTX 980]
                vendor: NVIDIA Corporation
                physical id: 0
                bus info: pci@0000:02:00.0
                version: a1
                width: 64 bits
                clock: 33MHz
                capabilities: pm msi pciexpress vga_controller bus_master cap_list rom
                configuration: driver=nvidia latency=0
                resources: irq:30 memory:f9000000-f9ffffff memory:b0000000-bfffffff memory:ce000000-cfffffff ioport:ef00(size=128) memory:c0000-dffff
           *-multimedia
                description: Audio device
                product: GM204 High Definition Audio Controller
                vendor: NVIDIA Corporation
                physical id: 0.1
                bus info: pci@0000:02:00.1
                version: a1
                width: 32 bits
                clock: 33MHz
                capabilities: pm msi pciexpress bus_master cap_list
                configuration: driver=snd_hda_intel latency=0
                resources: irq:17 memory:faffc000-faffffff
        *-pci:2
             description: PCI bridge
             product: 5520/X58 I/O Hub PCI Express Root Port 5
             vendor: Intel Corporation
             physical id: 5
             bus info: pci@0000:00:05.0
             version: 13
             width: 32 bits
             clock: 33MHz
             capabilities: pci msi pciexpress pm normal_decode cap_list
             configuration: driver=pcieport
             resources: irq:16
        *-pci:3
             description: PCI bridge
             product: 5520/5500/X58 I/O Hub PCI Express Root Port 7
             vendor: Intel Corporation
             physical id: 7
             bus info: pci@0000:00:07.0
             version: 13
             width: 32 bits
             clock: 33MHz
             capabilities: pci msi pciexpress pm normal_decode cap_list
             configuration: driver=pcieport
             resources: irq:16
        *-pci:4
             description: PCI bridge
             product: 7500/5520/5500/X58 I/O Hub PCI Express Root Port 9
             vendor: Intel Corporation
             physical id: 9
             bus info: pci@0000:00:09.0
             version: 13
             width: 32 bits
             clock: 33MHz
             capabilities: pci msi pciexpress pm normal_decode cap_list
             configuration: driver=pcieport
             resources: irq:16
        *-generic:0 UNCLAIMED
             description: PIC
             product: 7500/5520/5500/X58 Physical and Link Layer Registers Port 0
             vendor: Intel Corporation
             physical id: 10
             bus info: pci@0000:00:10.0
             version: 13
             width: 32 bits
             clock: 33MHz
             capabilities: 8259 cap_list
             configuration: latency=0
        *-generic:1 UNCLAIMED
             description: PIC
             product: 7500/5520/5500/X58 Routing and Protocol Layer Registers Port 0
             vendor: Intel Corporation
             physical id: 10.1
             bus info: pci@0000:00:10.1
             version: 13
             width: 32 bits
             clock: 33MHz
             capabilities: 8259
             configuration: latency=0
        *-generic:2 UNCLAIMED
             description: PIC
             product: 7500/5520/5500 Physical and Link Layer Registers Port 1
             vendor: Intel Corporation
             physical id: 11
             bus info: pci@0000:00:11.0
             version: 13
             width: 32 bits
             clock: 33MHz
             capabilities: 8259 cap_list
             configuration: latency=0
        *-generic:3 UNCLAIMED
             description: PIC
             product: 7500/5520/5500 Routing & Protocol Layer Register Port 1
             vendor: Intel Corporation
             physical id: 11.1
             bus info: pci@0000:00:11.1
             version: 13
             width: 32 bits
             clock: 33MHz
             capabilities: 8259
             configuration: latency=0
        *-generic:4 UNCLAIMED
             description: PIC
             product: 7500/5520/5500/X58 I/O Hub I/OxAPIC Interrupt Controller
             vendor: Intel Corporation
             physical id: 13
             bus info: pci@0000:00:13.0
             version: 13
             width: 32 bits
             clock: 33MHz
             capabilities: pm io_x_-apic bus_master cap_list
             configuration: latency=0
             resources: memory:fbfff000-fbffffff
        *-generic:5
             description: PIC
             product: 7500/5520/5500/X58 I/O Hub System Management Registers
             vendor: Intel Corporation
             physical id: 14
             bus info: pci@0000:00:14.0
             version: 13
             width: 32 bits
             clock: 33MHz
             capabilities: pciexpress 8259 cap_list
             configuration: driver=i7core_edac latency=0
             resources: irq:0
        *-generic:6 UNCLAIMED
             description: PIC
             product: 7500/5520/5500/X58 I/O Hub GPIO and Scratch Pad Registers
             vendor: Intel Corporation
             physical id: 14.1
             bus info: pci@0000:00:14.1
             version: 13
             width: 32 bits
             clock: 33MHz
             capabilities: pciexpress 8259 cap_list
             configuration: latency=0
        *-generic:7 UNCLAIMED
             description: PIC
             product: 7500/5520/5500/X58 I/O Hub Control Status and RAS Registers
             vendor: Intel Corporation
             physical id: 14.2
             bus info: pci@0000:00:14.2
             version: 13
             width: 32 bits
             clock: 33MHz
             capabilities: pciexpress 8259 cap_list
             configuration: latency=0
        *-generic:8 UNCLAIMED
             description: PIC
             product: 7500/5520/5500/X58 Trusted Execution Technology Registers
             vendor: Intel Corporation
             physical id: 15
             bus info: pci@0000:00:15.0
             version: 13
             width: 32 bits
             clock: 33MHz
             capabilities: io_x_-apic
             configuration: latency=0
        *-usb:0
             description: USB controller
             product: 82801JI (ICH10 Family) USB UHCI Controller #4
             vendor: Intel Corporation
             physical id: 1a
             bus info: pci@0000:00:1a.0
             version: 00
             width: 32 bits
             clock: 33MHz
             capabilities: uhci bus_master cap_list
             configuration: driver=uhci_hcd latency=0
             resources: irq:16 ioport:ff00(size=32)
           *-usbhost
                product: UHCI Host Controller
                vendor: Linux 4.10.0-37-generic uhci_hcd
                physical id: 1
                bus info: usb@3
                logical name: usb3
                version: 4.10
                capabilities: usb-1.10
                configuration: driver=hub slots=2 speed=12Mbit/s
        *-usb:1
             description: USB controller
             product: 82801JI (ICH10 Family) USB UHCI Controller #5
             vendor: Intel Corporation
             physical id: 1a.1
             bus info: pci@0000:00:1a.1
             version: 00
             width: 32 bits
             clock: 33MHz
             capabilities: uhci bus_master cap_list
             configuration: driver=uhci_hcd latency=0
             resources: irq:21 ioport:fe00(size=32)
           *-usbhost
                product: UHCI Host Controller
                vendor: Linux 4.10.0-37-generic uhci_hcd
                physical id: 1
                bus info: usb@4
                logical name: usb4
                version: 4.10
                capabilities: usb-1.10
                configuration: driver=hub slots=2 speed=12Mbit/s
        *-usb:2
             description: USB controller
             product: 82801JI (ICH10 Family) USB UHCI Controller #6
             vendor: Intel Corporation
             physical id: 1a.2
             bus info: pci@0000:00:1a.2
             version: 00
             width: 32 bits
             clock: 33MHz
             capabilities: uhci bus_master cap_list
             configuration: driver=uhci_hcd latency=0
             resources: irq:18 ioport:fd00(size=32)
           *-usbhost
                product: UHCI Host Controller
                vendor: Linux 4.10.0-37-generic uhci_hcd
                physical id: 1
                bus info: usb@5
                logical name: usb5
                version: 4.10
                capabilities: usb-1.10
                configuration: driver=hub slots=2 speed=12Mbit/s
        *-usb:3
             description: USB controller
             product: 82801JI (ICH10 Family) USB2 EHCI Controller #2
             vendor: Intel Corporation
             physical id: 1a.7
             bus info: pci@0000:00:1a.7
             version: 00
             width: 32 bits
             clock: 33MHz
             capabilities: pm debug ehci bus_master cap_list
             configuration: driver=ehci-pci latency=0
             resources: irq:18 memory:fbffe000-fbffe3ff
           *-usbhost
                product: EHCI Host Controller
                vendor: Linux 4.10.0-37-generic ehci_hcd
                physical id: 1
                bus info: usb@1
                logical name: usb1
                version: 4.10
                capabilities: usb-2.00
                configuration: driver=hub slots=6 speed=480Mbit/s
        *-multimedia
             description: Audio device
             product: 82801JI (ICH10 Family) HD Audio Controller
             vendor: Intel Corporation
             physical id: 1b
             bus info: pci@0000:00:1b.0
             version: 00
             width: 64 bits
             clock: 33MHz
             capabilities: pm msi pciexpress bus_master cap_list
             configuration: driver=snd_hda_intel latency=0
             resources: irq:29 memory:fbff4000-fbff7fff
        *-pci:5
             description: PCI bridge
             product: 82801JI (ICH10 Family) PCI Express Root Port 1
             vendor: Intel Corporation
             physical id: 1c
             bus info: pci@0000:00:1c.0
             version: 00
             width: 32 bits
             clock: 33MHz
             capabilities: pci pciexpress msi pm normal_decode bus_master cap_list
             configuration: driver=pcieport
             resources: irq:24 ioport:1000(size=4096) memory:d0000000-d01fffff ioport:d0200000(size=2097152)
        *-pci:6
             description: PCI bridge
             product: 82801JI (ICH10 Family) PCI Express Port 2
             vendor: Intel Corporation
             physical id: 1c.1
             bus info: pci@0000:00:1c.1
             version: 00
             width: 32 bits
             clock: 33MHz
             capabilities: pci pciexpress msi pm normal_decode bus_master cap_list
             configuration: driver=pcieport
             resources: irq:25 ioport:d000(size=4096) memory:fbe00000-fbefffff ioport:d0400000(size=2097152)
           *-storage
                description: SATA controller
                product: JMB363 SATA/IDE Controller
                vendor: JMicron Technology Corp.
                physical id: 0
                bus info: pci@0000:07:00.0
                version: 02
                width: 32 bits
                clock: 33MHz
                capabilities: storage pm pciexpress ahci_1.0 bus_master cap_list
                configuration: driver=ahci latency=0
                resources: irq:17 memory:fbefe000-fbefffff
           *-ide
                description: IDE interface
                product: JMB363 SATA/IDE Controller
                vendor: JMicron Technology Corp.
                physical id: 0.1
                bus info: pci@0000:07:00.1
                version: 02
                width: 32 bits
                clock: 33MHz
                capabilities: ide pm bus_master cap_list
                configuration: driver=pata_jmicron latency=0
                resources: irq:18 ioport:df00(size=8) ioport:de00(size=4) ioport:dd00(size=8) ioport:dc00(size=4) ioport:db00(size=16)
        *-pci:7
             description: PCI bridge
             product: 82801JI (ICH10 Family) PCI Express Root Port 5
             vendor: Intel Corporation
             physical id: 1c.4
             bus info: pci@0000:00:1c.4
             version: 00
             width: 32 bits
             clock: 33MHz
             capabilities: pci pciexpress msi pm normal_decode bus_master cap_list
             configuration: driver=pcieport
             resources: irq:26 ioport:c000(size=4096) memory:fbc00000-fbcfffff ioport:fbb00000(size=1048576)
           *-network
                description: Ethernet interface
                product: RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller
                vendor: Realtek Semiconductor Co., Ltd.
                physical id: 0
                bus info: pci@0000:08:00.0
                logical name: enp8s0
                version: 02
                serial: 00:24:1d:c0:b5:95
                size: 100Mbit/s
                capacity: 1Gbit/s
                width: 64 bits
                clock: 33MHz
                capabilities: pm msi pciexpress msix vpd bus_master cap_list rom ethernet physical tp mii 10bt 10bt-fd 100bt 100bt-fd 1000bt 1000bt-fd autonegotiation
                configuration: autonegotiation=on broadcast=yes driver=r8169 driverversion=2.3LK-NAPI duplex=full ip=158.108.38.92 latency=0 link=yes multicast=yes port=MII speed=100Mbit/s
                resources: irq:28 ioport:ce00(size=256) memory:fbbff000-fbbfffff memory:fbbe0000-fbbeffff memory:fbc00000-fbc0ffff
        *-usb:4
             description: USB controller
             product: 82801JI (ICH10 Family) USB UHCI Controller #1
             vendor: Intel Corporation
             physical id: 1d
             bus info: pci@0000:00:1d.0
             version: 00
             width: 32 bits
             clock: 33MHz
             capabilities: uhci bus_master cap_list
             configuration: driver=uhci_hcd latency=0
             resources: irq:23 ioport:fc00(size=32)
           *-usbhost
                product: UHCI Host Controller
                vendor: Linux 4.10.0-37-generic uhci_hcd
                physical id: 1
                bus info: usb@6
                logical name: usb6
                version: 4.10
                capabilities: usb-1.10
                configuration: driver=hub slots=2 speed=12Mbit/s
        *-usb:5
             description: USB controller
             product: 82801JI (ICH10 Family) USB UHCI Controller #2
             vendor: Intel Corporation
             physical id: 1d.1
             bus info: pci@0000:00:1d.1
             version: 00
             width: 32 bits
             clock: 33MHz
             capabilities: uhci bus_master cap_list
             configuration: driver=uhci_hcd latency=0
             resources: irq:19 ioport:fb00(size=32)
           *-usbhost
                product: UHCI Host Controller
                vendor: Linux 4.10.0-37-generic uhci_hcd
                physical id: 1
                bus info: usb@7
                logical name: usb7
                version: 4.10
                capabilities: usb-1.10
                configuration: driver=hub slots=2 speed=12Mbit/s
        *-usb:6
             description: USB controller
             product: 82801JI (ICH10 Family) USB UHCI Controller #3
             vendor: Intel Corporation
             physical id: 1d.2
             bus info: pci@0000:00:1d.2
             version: 00
             width: 32 bits
             clock: 33MHz
             capabilities: uhci bus_master cap_list
             configuration: driver=uhci_hcd latency=0
             resources: irq:18 ioport:fa00(size=32)
           *-usbhost
                product: UHCI Host Controller
                vendor: Linux 4.10.0-37-generic uhci_hcd
                physical id: 1
                bus info: usb@8
                logical name: usb8
                version: 4.10
                capabilities: usb-1.10
                configuration: driver=hub slots=2 speed=12Mbit/s
        *-usb:7
             description: USB controller
             product: 82801JI (ICH10 Family) USB2 EHCI Controller #1
             vendor: Intel Corporation
             physical id: 1d.7
             bus info: pci@0000:00:1d.7
             version: 00
             width: 32 bits
             clock: 33MHz
             capabilities: pm debug ehci bus_master cap_list
             configuration: driver=ehci-pci latency=0
             resources: irq:23 memory:fbffd000-fbffd3ff
           *-usbhost
                product: EHCI Host Controller
                vendor: Linux 4.10.0-37-generic ehci_hcd
                physical id: 1
                bus info: usb@2
                logical name: usb2
                version: 4.10
                capabilities: usb-2.00
                configuration: driver=hub slots=6 speed=480Mbit/s
        *-pci:8
             description: PCI bridge
             product: 82801 PCI Bridge
             vendor: Intel Corporation
             physical id: 1e
             bus info: pci@0000:00:1e.0
             version: 90
             width: 32 bits
             clock: 33MHz
             capabilities: pci subtractive_decode bus_master cap_list
             resources: memory:fbd00000-fbdfffff
           *-firewire
                description: FireWire (IEEE 1394)
                product: TSB43AB23 IEEE-1394a-2000 Controller (PHY/Link)
                vendor: Texas Instruments
                physical id: 6
                bus info: pci@0000:09:06.0
                version: 00
                width: 32 bits
                clock: 33MHz
                capabilities: pm ohci bus_master cap_list
                configuration: driver=firewire_ohci latency=32 maxlatency=4 mingnt=2
                resources: irq:18 memory:fbdff000-fbdff7ff memory:fbdf8000-fbdfbfff
        *-isa
             description: ISA bridge
             product: 82801JIR (ICH10R) LPC Interface Controller
             vendor: Intel Corporation
             physical id: 1f
             bus info: pci@0000:00:1f.0
             version: 00
             width: 32 bits
             clock: 33MHz
             capabilities: isa bus_master cap_list
             configuration: driver=lpc_ich latency=0
             resources: irq:0
        *-storage
             description: SATA controller
             product: 82801JI (ICH10 Family) SATA AHCI Controller
             vendor: Intel Corporation
             physical id: 1f.2
             bus info: pci@0000:00:1f.2
             version: 00
             width: 32 bits
             clock: 66MHz
             capabilities: storage msi pm ahci_1.0 bus_master cap_list
             configuration: driver=ahci latency=0
             resources: irq:27 ioport:f900(size=8) ioport:f800(size=4) ioport:f700(size=8) ioport:f600(size=4) ioport:f500(size=32) memory:fbffc000-fbffc7ff
        *-serial UNCLAIMED
             description: SMBus
             product: 82801JI (ICH10 Family) SMBus Controller
             vendor: Intel Corporation
             physical id: 1f.3
             bus info: pci@0000:00:1f.3
             version: 00
             width: 64 bits
             clock: 33MHz
             configuration: latency=0
             resources: memory:fbffb000-fbffb0ff ioport:500(size=32)
     *-pci:1
          description: Host bridge
          product: Xeon 5500/Core i7 QuickPath Architecture Generic Non-Core Registers
          vendor: Intel Corporation
          physical id: 101
          bus info: pci@0000:ff:00.0
          version: 05
          width: 32 bits
          clock: 33MHz
     *-pci:2
          description: Host bridge
          product: Xeon 5500/Core i7 QuickPath Architecture System Address Decoder
          vendor: Intel Corporation
          physical id: 102
          bus info: pci@0000:ff:00.1
          version: 05
          width: 32 bits
          clock: 33MHz
     *-pci:3
          description: Host bridge
          product: Xeon 5500/Core i7 QPI Link 0
          vendor: Intel Corporation
          physical id: 103
          bus info: pci@0000:ff:02.0
          version: 05
          width: 32 bits
          clock: 33MHz
     *-pci:4
          description: Host bridge
          product: Xeon 5500/Core i7 QPI Physical 0
          vendor: Intel Corporation
          physical id: 104
          bus info: pci@0000:ff:02.1
          version: 05
          width: 32 bits
          clock: 33MHz
     *-pci:5
          description: Host bridge
          product: Xeon 5500/Core i7 Integrated Memory Controller
          vendor: Intel Corporation
          physical id: 105
          bus info: pci@0000:ff:03.0
          version: 05
          width: 32 bits
          clock: 33MHz
     *-pci:6
          description: Host bridge
          product: Xeon 5500/Core i7 Integrated Memory Controller Target Address Decoder
          vendor: Intel Corporation
          physical id: 106
          bus info: pci@0000:ff:03.1
          version: 05
          width: 32 bits
          clock: 33MHz
     *-pci:7
          description: Host bridge
          product: Xeon 5500/Core i7 Integrated Memory Controller Test Registers
          vendor: Intel Corporation
          physical id: 107
          bus info: pci@0000:ff:03.4
          version: 05
          width: 32 bits
          clock: 33MHz
     *-pci:8
          description: Host bridge
          product: Xeon 5500/Core i7 Integrated Memory Controller Channel 0 Control Registers
          vendor: Intel Corporation
          physical id: 108
          bus info: pci@0000:ff:04.0
          version: 05
          width: 32 bits
          clock: 33MHz
     *-pci:9
          description: Host bridge
          product: Xeon 5500/Core i7 Integrated Memory Controller Channel 0 Address Registers
          vendor: Intel Corporation
          physical id: 109
          bus info: pci@0000:ff:04.1
          version: 05
          width: 32 bits
          clock: 33MHz
     *-pci:10
          description: Host bridge
          product: Xeon 5500/Core i7 Integrated Memory Controller Channel 0 Rank Registers
          vendor: Intel Corporation
          physical id: 10a
          bus info: pci@0000:ff:04.2
          version: 05
          width: 32 bits
          clock: 33MHz
     *-pci:11
          description: Host bridge
          product: Xeon 5500/Core i7 Integrated Memory Controller Channel 0 Thermal Control Registers
          vendor: Intel Corporation
          physical id: 10b
          bus info: pci@0000:ff:04.3
          version: 05
          width: 32 bits
          clock: 33MHz
     *-pci:12
          description: Host bridge
          product: Xeon 5500/Core i7 Integrated Memory Controller Channel 1 Control Registers
          vendor: Intel Corporation
          physical id: 10c
          bus info: pci@0000:ff:05.0
          version: 05
          width: 32 bits
          clock: 33MHz
     *-pci:13
          description: Host bridge
          product: Xeon 5500/Core i7 Integrated Memory Controller Channel 1 Address Registers
          vendor: Intel Corporation
          physical id: 10d
          bus info: pci@0000:ff:05.1
          version: 05
          width: 32 bits
          clock: 33MHz
     *-pci:14
          description: Host bridge
          product: Xeon 5500/Core i7 Integrated Memory Controller Channel 1 Rank Registers
          vendor: Intel Corporation
          physical id: 10e
          bus info: pci@0000:ff:05.2
          version: 05
          width: 32 bits
          clock: 33MHz
     *-pci:15
          description: Host bridge
          product: Xeon 5500/Core i7 Integrated Memory Controller Channel 1 Thermal Control Registers
          vendor: Intel Corporation
          physical id: 10f
          bus info: pci@0000:ff:05.3
          version: 05
          width: 32 bits
          clock: 33MHz
     *-pci:16
          description: Host bridge
          product: Xeon 5500/Core i7 Integrated Memory Controller Channel 2 Control Registers
          vendor: Intel Corporation
          physical id: 110
          bus info: pci@0000:ff:06.0
          version: 05
          width: 32 bits
          clock: 33MHz
     *-pci:17
          description: Host bridge
          product: Xeon 5500/Core i7 Integrated Memory Controller Channel 2 Address Registers
          vendor: Intel Corporation
          physical id: 111
          bus info: pci@0000:ff:06.1
          version: 05
          width: 32 bits
          clock: 33MHz
     *-pci:18
          description: Host bridge
          product: Xeon 5500/Core i7 Integrated Memory Controller Channel 2 Rank Registers
          vendor: Intel Corporation
          physical id: 112
          bus info: pci@0000:ff:06.2
          version: 05
          width: 32 bits
          clock: 33MHz
     *-pci:19
          description: Host bridge
          product: Xeon 5500/Core i7 Integrated Memory Controller Channel 2 Thermal Control Registers
          vendor: Intel Corporation
          physical id: 113
          bus info: pci@0000:ff:06.3
          version: 05
          width: 32 bits
          clock: 33MHz
     *-scsi:0
          physical id: 1
          logical name: scsi8
          capabilities: emulated
        *-disk
             description: ATA Disk
             product: ST3160815AS
             vendor: Seagate
             physical id: 0.0.0
             bus info: scsi@8:0.0.0
             logical name: /dev/sda
             version: H
             serial: 9RXFLPH5
             size: 149GiB (160GB)
             capabilities: partitioned partitioned:dos
             configuration: ansiversion=5 logicalsectorsize=512 sectorsize=512 signature=7089ff6c
           *-volume:0
                description: EXT4 volume
                vendor: Linux
                physical id: 1
                bus info: scsi@8:0.0.0,1
                logical name: /dev/sda1
                logical name: /
                logical name: /var/lib/docker/plugins
                logical name: /var/lib/docker/aufs
                version: 1.0
                serial: 02d4568d-e114-4ee1-95a0-7a7aaf1fc5d0
                size: 141GiB
                capacity: 141GiB
                capabilities: primary bootable journaled extended_attributes large_files huge_files dir_nlink extents ext4 ext2 initialized
                configuration: created=2016-08-22 14:01:46 filesystem=ext4 lastmountpoint=/ modified=2017-11-08 03:18:59 mount.fstype=ext4 mount.options=rw,relatime,grpquota,errors=remount-ro,data=ordered mounted=2017-10-30 15:54:07 state=mounted
           *-volume:1
                description: Extended partition
                physical id: 2
                bus info: scsi@8:0.0.0,2
                logical name: /dev/sda2
                size: 8189MiB
                capacity: 8189MiB
                capabilities: primary extended partitioned partitioned:extended
              *-logicalvolume
                   description: Linux swap volume
                   physical id: 5
                   logical name: /dev/sda5
                   version: 1
                   serial: e14bbc05-b40c-4e2f-9afa-f37208cef7ae
                   size: 8189MiB
                   capacity: 8189MiB
                   capabilities: nofs swap initialized
                   configuration: filesystem=swap pagesize=4096
     *-scsi:1
          physical id: 2
          logical name: scsi9
          capabilities: emulated
        *-disk
             description: ATA Disk
             product: WDC WD2500AAJS-2
             vendor: Western Digital
             physical id: 0.0.0
             bus info: scsi@9:0.0.0
             logical name: /dev/sdb
             version: 1B01
             serial: WD-WMART1823227
             size: 232GiB (250GB)
             capabilities: partitioned partitioned:dos
             configuration: ansiversion=5 logicalsectorsize=512 sectorsize=512 signature=e421264c
           *-volume:0
                description: Windows NTFS volume
                physical id: 1
                bus info: scsi@9:0.0.0,1
                logical name: /dev/sdb1
                version: 3.1
                serial: 8062-5560
                size: 498MiB
                capacity: 500MiB
                capabilities: primary bootable ntfs initialized
                configuration: clustersize=4096 created=2017-01-19 20:53:16 filesystem=ntfs label=System Reserved modified_by_chkdsk=true mounted_on_nt4=true resize_log_file=true state=dirty upgrade_on_mount=true
           *-volume:1
                description: Windows NTFS volume
                physical id: 2
                bus info: scsi@9:0.0.0,2
                logical name: /dev/sdb2
                version: 3.1
                serial: c6a00d30-0f7a-df40-8268-03671c1ab1f8
                size: 232GiB
                capacity: 232GiB
                capabilities: primary ntfs initialized
                configuration: clustersize=4096 created=2017-01-19 20:53:29 filesystem=ntfs state=clean
  *-network:0
       description: Ethernet interface
       physical id: 1
       logical name: veth4b14fde
       serial: 6e:1c:7a:15:0f:0a
       size: 10Gbit/s
       capabilities: ethernet physical
       configuration: autonegotiation=off broadcast=yes driver=veth driverversion=1.0 duplex=full link=yes multicast=yes port=twisted pair speed=10Gbit/s
  *-network:1
       description: Ethernet interface
       physical id: 2
       logical name: veth8cc25ee
       serial: 52:98:e2:c8:ce:6d
       size: 10Gbit/s
       capabilities: ethernet physical
       configuration: autonegotiation=off broadcast=yes driver=veth driverversion=1.0 duplex=full link=yes multicast=yes port=twisted pair speed=10Gbit/s
  *-network:2
       description: Ethernet interface
       physical id: 3
       logical name: docker_gwbridge
       serial: 02:42:6f:4b:3c:5e
       capabilities: ethernet physical
       configuration: broadcast=yes driver=bridge driverversion=2.3 firmware=N/A ip=172.18.0.1 link=yes multicast=yes
  *-network:3
       description: Ethernet interface
       physical id: 4
       logical name: docker0
       serial: 02:42:0c:50:7c:60
       capabilities: ethernet physical
       configuration: broadcast=yes driver=bridge driverversion=2.3 firmware=N/A ip=172.17.0.1 link=yes multicast=yes
   ```