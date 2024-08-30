<?xml version='1.0' encoding='utf-8'?>
<scheme version="2.0" title="Preprocess EEG Compute Bandpower" description="This pipeline preprocesses and cleans the EEG, then computes the average power across channels in a moving window for a specific frequency band, and then both plots it and sends it out over the network for pickup by another application (i.e., a game) &#10;&#10;It also demonstrates a way of compting spectral power for multiple bands at once.">
	<nodes>
		<node id="0" name="LSL Input" qualified_name="widgets.network.owlslinput.OWLSLInput" project_name="NeuroPype" version="1.5.2" title="LSL Input" uuid="ddde8ae0-2067-408d-91af-6ac6cfa67be5" position="(-400, 400)" />
		<node id="1" name="Dejitter Timestamps" qualified_name="widgets.utilities.owdejittertimestamps.OWDejitterTimestamps" project_name="NeuroPype" version="1.0.0" title="Dejitter Timestamps" uuid="9b4ed036-bd52-431d-8e63-c5ffa9945574" position="(-300, 400)" />
		<node id="2" name="FIR Filter" qualified_name="widgets.signal_processing.owfirfilter.OWFIRFilter" project_name="NeuroPype" version="1.1.1" title="FIR Bandpass 3.5-30Hz" uuid="87872058-9fc4-4fde-aa1a-122b3111f6f1" position="(-100, 400)" />
		<node id="3" name="Assign Channel Locations" qualified_name="widgets.source_localization.owassignchannellocations.OWAssignChannelLocations" project_name="NeuroPype" version="1.2.0" title="Assign Channel Locations" uuid="b23007f3-c00e-443a-bd2e-eea6c4b7861f" position="(0, 400)" />
		<node id="4" name="Remove Unlocalized Channels" qualified_name="widgets.source_localization.owremoveunlocalizedchannels.OWRemoveUnlocalizedChannels" project_name="NeuroPype" version="1.2.0" title="Remove Unlocalized Channels&#10;[]" uuid="da45c1be-73e0-4a87-a3c3-20406007418e" position="(100, 400)" />
		<node id="5" name="Extract Channel Names" qualified_name="widgets.utilities.owextractchannels.OWExtractChannels" project_name="NeuroPype" version="1.0.1" title="Extract Channel Names" uuid="011f6889-a743-4d17-bdeb-fec4c8b19353" position="(300, 300)" />
		<node id="6" name="Bad Channel Removal" qualified_name="widgets.neural.owbadchannelremoval.OWBadChannelRemoval" project_name="NeuroPype" version="1.2.0" title="Bad Channel Removal&#10;[corr&lt;0.8,noise&gt;4.0 st.]" uuid="6e5e379b-a866-458e-b0ee-1e99f682f32b" position="(200, 400)" />
		<node id="7" name="Interpolate Missing Channels" qualified_name="widgets.neural.owinterpolatemissingchannels.OWInterpolateMissingChannels" project_name="NeuroPype" version="1.5.0" title="Interpolate Missing Channels&#10;[montage: auto (spherical-spline)]" uuid="d46625a7-a3f4-4bea-a676-b18b6f200cad" position="(500, 400)" />
		<node id="8" name="Artifact Removal" qualified_name="widgets.neural.owartifactremoval.OWArtifactRemoval" project_name="NeuroPype" version="2.4.1" title="Artifact Removal&#10;[cutoff:7.5]" uuid="5e929147-ef80-456b-b468-de9611e0eb22" position="(300, 400)" />
		<node id="9" name="Segmentation" qualified_name="widgets.formatting.owsegmentation.OWSegmentation" project_name="NeuroPype" version="1.0.2" title="Segmentation&#10;[[-1, 0]]" uuid="0d2860e7-a8fc-4ab0-97ae-3f7ef37e9122" position="(1100, 400)" />
		<node id="10" name="Combine Channels" qualified_name="widgets.signal_processing.owcombinechannels.OWCombineChannels" project_name="NeuroPype" version="1.1.0" title="leftIFG (F7,FC5)" uuid="f4f339af-e1e5-40d9-8f0b-356f9c07290b" position="(600, 300)" />
		<node id="11" name="Continuous Wavelet Transform" qualified_name="widgets.spectral.owcontinuouswavelettransform.OWContinuousWaveletTransform" project_name="NeuroPype" version="1.0.0" title="Continuous Wavelet Transform&#10;[morl, scales:[6, 70]]" uuid="354fe84d-cba2-42f2-845e-4eb0be3a30a7" position="(1200, 400)" />
		<node id="12" name="IIR Filter" qualified_name="widgets.signal_processing.owiirfilter.OWIIRFilter" project_name="NeuroPype" version="1.1.0" title="IIR Notch 48-52Hz" uuid="e578edcc-d5b2-4ae2-88ca-6a23511441db" position="(-200, 400)" />
		<node id="13" name="Coherence" qualified_name="widgets.spectral.owcoherence.OWCoherence" project_name="NeuroPype" version="1.0.0" title="Coherence" uuid="b1e607ed-5be4-49b3-a8dc-e43f8f1c1c4e" position="(1300, 400)" />
		<node id="14" name="Select Range" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" project_name="NeuroPype" version="1.4.0" title="Select Range&#10;[7...19 along frequency (indices)]" uuid="f134a084-140c-4e7d-9e78-27e0a4c27618" position="(1400, 400)" />
		<node id="15" name="Mean" qualified_name="widgets.statistics.owmean.OWMean" project_name="NeuroPype" version="1.1.0" title="Mean&#10;[over frequency]" uuid="158b7c87-5162-4de7-9380-c1fd3946462d" position="(1500, 400)" />
		<node id="16" name="Play back REC" qualified_name="widgets.file_system.owplaybackrec.OWPlayBackREC" project_name="NeuroPype" version="1.0.0" title="Play back REC" uuid="3c57e364-a9b7-4c1d-acca-1cdb385958a5" position="(-400, 500)" />
		<node id="17" name="Select Range" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" project_name="NeuroPype" version="1.4.0" title="Select Range&#10;[['ActiChamp_0-rightIFG'] along named (auto)]" uuid="315ca1a0-1952-4929-9e27-2ad691e2b917" position="(1600, 400)" />
		<node id="18" name="LSL Output" qualified_name="widgets.network.owlsloutput.OWLSLOutput" project_name="NeuroPype" version="1.4.3" title="LSL Output&#10;[IFG (coherence); id:&quot;IFG&quot;]" uuid="db82e902-af09-47a5-8a64-44d9637b49d5" position="(1700, 400)" />
		<node id="19" name="Record to CSV" qualified_name="widgets.file_system.owrecordtocsv.OWRecordToCSV" project_name="NeuroPype" version="1.0.1" title="Record to CSV" uuid="c9e258f6-acbf-4588-a62d-cd91348498c1" position="(1700, 300)" />
		<node id="20" name="Re-referencing" qualified_name="widgets.signal_processing.owrereferencing.OWRereferencing" project_name="NeuroPype" version="1.1.0" title="Re-referencing&#10;[['Fz'] along named]" uuid="05f4cc05-662c-47ce-b387-eaf7b7a77fb4" position="(700, 300)" />
		<node id="21" name="Merge Streams" qualified_name="widgets.formatting.owmergestreams.OWMergeStreams" project_name="NeuroPype" version="1.0.0" title="Merge Streams&#10;[]" uuid="32998a1d-b5c7-44ae-8521-cb33b7aeb0de" position="(900, 400)" />
		<node id="22" name="Fuse Streams" qualified_name="widgets.formatting.owfusestreams.OWFuseStreams" project_name="NeuroPype" version="0.9.6" title="Fuse Streams" uuid="769078bc-0c19-4db0-8324-74ce51141530" position="(1000, 400)" />
		<node id="23" name="Select Range" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" project_name="NeuroPype" version="1.4.0" title="Select Range&#10;[['leftIFG'] along named (names)]" uuid="d5a364a5-881c-4b5b-a69e-3e4756c892af" position="(800, 300)" />
		<node id="24" name="Select Range" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" project_name="NeuroPype" version="1.4.0" title="Select Range&#10;[['rightIFG'] along named (names)]" uuid="b9bac4d2-2d22-4254-a876-78f9e0c0bf9f" position="(800, 500)" />
		<node id="25" name="Combine Channels" qualified_name="widgets.signal_processing.owcombinechannels.OWCombineChannels" project_name="NeuroPype" version="1.1.0" title="rightIFG (F8,FC6)" uuid="deb97ab5-8239-4fab-84a3-9cca55706f45" position="(600, 500)" />
		<node id="26" name="Re-referencing" qualified_name="widgets.signal_processing.owrereferencing.OWRereferencing" project_name="NeuroPype" version="1.1.0" title="Re-referencing&#10;[['AFz'] along named]" uuid="02098fe1-c1c5-487b-9b7c-53bc31f6e772" position="(698.8888888888889, 498.8888888888889)" />
	</nodes>
	<links>
		<link id="0" source_node_id="6" sink_node_id="8" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="1" source_node_id="4" sink_node_id="6" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="2" source_node_id="8" sink_node_id="7" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="3" source_node_id="4" sink_node_id="5" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="4" source_node_id="5" sink_node_id="7" source_channel="Channel Names" sink_channel="Desired Channels" enabled="true" />
		<link id="5" source_node_id="3" sink_node_id="4" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="6" source_node_id="12" sink_node_id="2" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="7" source_node_id="1" sink_node_id="12" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="8" source_node_id="14" sink_node_id="15" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="9" source_node_id="17" sink_node_id="18" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="10" source_node_id="21" sink_node_id="22" source_channel="Outdata" sink_channel="Data" enabled="true" />
		<link id="11" source_node_id="20" sink_node_id="23" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="12" source_node_id="15" sink_node_id="17" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="13" source_node_id="26" sink_node_id="24" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="14" source_node_id="10" sink_node_id="20" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="15" source_node_id="25" sink_node_id="26" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="16" source_node_id="9" sink_node_id="11" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="17" source_node_id="11" sink_node_id="13" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="18" source_node_id="22" sink_node_id="9" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="19" source_node_id="13" sink_node_id="14" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="20" source_node_id="2" sink_node_id="3" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="21" source_node_id="7" sink_node_id="10" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="22" source_node_id="7" sink_node_id="25" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="23" source_node_id="23" sink_node_id="21" source_channel="Data" sink_channel="Data1" enabled="true" />
		<link id="24" source_node_id="24" sink_node_id="21" source_channel="Data" sink_channel="Data2" enabled="true" />
		<link id="25" source_node_id="0" sink_node_id="1" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="26" source_node_id="17" sink_node_id="19" source_channel="Data" sink_channel="Data" enabled="true" />
	</links>
	<annotations>
		<text id="0" rect="(462.96468133333326, 99.7680633333334, 276.4157261111113, 88.7777777777778)" font-family="DejaVu Sans Mono" font-size="16">Agrupamiento de canales cercanos en regiones (tanto del participante izquierdo - impares; como del participante derecho - pares)</text>
		<arrow id="1" start="(28.933999999999855, 152.0626666666667)" end="(59.73822222222222, 328.7241111111111)" fill="#C1272D" />
		<text id="2" rect="(-73.26977777777779, 116.77100000000003, 204.97399999999993, 31.0)" font-family="DejaVu Sans Mono" font-size="16">Pre-procesamiento general</text>
		<text id="3" rect="(1348.8888888888898, 248.8888888888888, 93.33333333333371, 50.0)" font-family="DejaVu Sans Mono" font-size="16">Banda Teta
(4-8 Hz)</text>
		<arrow id="4" start="(1395.5555555555563, 299.9999999999997)" end="(1396.6666666666677, 363.3333333333331)" fill="#C1272D" />
		<arrow id="5" start="(601.1111111111117, 193.33333333333337)" end="(601.1111111111115, 262.22222222222223)" fill="#C1272D" />
		<text id="6" rect="(1475.5555555555554, 154.44444444444423, 226.66666666666697, 88.0)" font-family="DejaVu Sans Mono" font-size="16">Selecciona solo el valor de coherencia (ignora el 1.0 por compararse a si mismo)</text>
		<arrow id="7" start="(1588.8888888888882, 247.77777777777766)" end="(1599.9999999999998, 363.3333333333332)" fill="#C1272D" />
	</annotations>
	<thumbnail />
	<node_properties>
		<properties node_id="0" format="pickle">gASVOwIAAAAAAAB9lCiMDWNoYW5uZWxfbmFtZXOUXZSMCmRhdGFfZHR5cGWUjAdmbG9hdDY0lIwL
ZGlhZ25vc3RpY3OUiYwTZXhjbHVkZV9kZXNjX2ZpZWxkc5RdlIwObG9jYWxob3N0X29ubHmUiYwM
bWFya2VyX3F1ZXJ5lIwAlIwMbWF4X2Jsb2NrbGVulE0ABIwKbWF4X2J1ZmxlbpRLHowMbWF4X2No
dW5rbGVulEsAjAhtZXRhZGF0YZR9lIwMbm9taW5hbF9yYXRllIwNKHVzZSBkZWZhdWx0KZSMCW9t
aXRfZGVzY5SJjA9wcmVhbGxvY19idWZmZXKUiIwOcHJvY19jbG9ja3N5bmOUiIwNcHJvY19kZWpp
dHRlcpSJjA9wcm9jX21vbm90b25pemWUiYwPcHJvY190aHJlYWRzYWZllImMBXF1ZXJ5lIwKdHlw
ZT0nRUVHJ5SMB3JlY292ZXKUiIwUcmVzb2x2ZV9taW5pbXVtX3RpbWWURz/gAAAAAAAAjBNzYXZl
ZFdpZGdldEdlb21ldHJ5lIwDc2lwlIwOX3VucGlja2xlX3R5cGWUk5SMDFB5UXQ1LlF0Q29yZZSM
ClFCeXRlQXJyYXmUQ0IB2dDLAAMAAAAAAwsAAACNAAAEdAAAA0kAAAMMAAAAswAABHMAAANIAAAA
AAAAAAAHgAAAAwwAAACzAAAEcwAAA0iUhZSHlFKUjA5zZXRfYnJlYWtwb2ludJSJjA91c2Vfc3Ry
ZWFtbmFtZXOUiXUu
</properties>
		<properties node_id="1" format="pickle">gASVCwEAAAAAAAB9lCiMD2ZvcmNlX21vbm90b25pY5SIjA9mb3JnZXRfaGFsZnRpbWWUS1qMDm1h
eF91cGRhdGVyYXRllE30AYwIbWV0YWRhdGGUfZSME3NhdmVkV2lkZ2V0R2VvbWV0cnmUjANzaXCU
jA5fdW5waWNrbGVfdHlwZZSTlIwMUHlRdDUuUXRDb3JllIwKUUJ5dGVBcnJheZRDQgHZ0MsAAwAA
AAAJSwAAASMAAAq0AAACjgAACUwAAAFCAAAKswAAAo0AAAABAAAAAAUAAAAJTAAAAUIAAAqzAAAC
jZSFlIeUUpSMDnNldF9icmVha3BvaW50lImMDndhcm11cF9zYW1wbGVzlEr/////dS4=
</properties>
		<properties node_id="2" format="pickle">gASVmgEAAAAAAAB9lCiMDWFudGlzeW1tZXRyaWOUiYwEYXhpc5SMBHRpbWWUjBJjb252b2x1dGlv
bl9tZXRob2SUjAhzdGFuZGFyZJSMDmN1dF9wcmVyaW5naW5nlImMCWRpcmVjdGlvbpSMB2Zvcndh
cmSUjAtmcmVxdWVuY2llc5RdlChHQAgAAAAAAABHQAwAAAAAAABLHksjZYwIbWV0YWRhdGGUfZSM
DW1pbmltdW1fcGhhc2WUiIwEbW9kZZSMCGJhbmRwYXNzlIwFb3JkZXKUjA0odXNlIGRlZmF1bHQp
lIwTc2F2ZWRXaWRnZXRHZW9tZXRyeZSMA3NpcJSMDl91bnBpY2tsZV90eXBllJOUjAxQeVF0NS5R
dENvcmWUjApRQnl0ZUFycmF5lENCAdnQywADAAAAAALfAAAAWQAABKIAAAPtAAAC3wAAAFkAAASi
AAAD7QAAAAAAAAAAB4AAAALfAAAAWQAABKIAAAPtlIWUh5RSlIwOc2V0X2JyZWFrcG9pbnSUiYwK
c3RvcF9hdHRlbpRHQEkAAAAAAAB1Lg==
</properties>
		<properties node_id="3" format="pickle">gASV7wAAAAAAAAB9lCiMDmZvcmNlX292ZXJyaWRllIiMCG1ldGFkYXRhlH2UjAdtb250YWdllIwA
lIwMbW9udGFnZV90eXBllIwEYXV0b5SME3NhdmVkV2lkZ2V0R2VvbWV0cnmUjANzaXCUjA5fdW5w
aWNrbGVfdHlwZZSTlIwMUHlRdDUuUXRDb3JllIwKUUJ5dGVBcnJheZRDQgHZ0MsAAwAAAAADDAAA
AUMAAATRAAAC8gAAAw0AAAFpAAAE0AAAAvEAAAAAAAAAAAeAAAADDQAAAWkAAATQAAAC8ZSFlIeU
UpSMDnNldF9icmVha3BvaW50lIl1Lg==
</properties>
		<properties node_id="4" format="pickle">gASVzwAAAAAAAAB9lCiMCG1ldGFkYXRhlH2UjBBwcm90ZWN0X2NoYW5uZWxzlF2UjBNzYXZlZFdp
ZGdldEdlb21ldHJ5lIwDc2lwlIwOX3VucGlja2xlX3R5cGWUk5SMDFB5UXQ1LlF0Q29yZZSMClFC
eXRlQXJyYXmUQ0IB2dDLAAMAAAAAAwsAAAFtAAAEdAAAAmoAAAMMAAABkwAABHMAAAJpAAAAAAAA
AAAHgAAAAwwAAAGTAAAEcwAAAmmUhZSHlFKUjA5zZXRfYnJlYWtwb2ludJSJdS4=
</properties>
		<properties node_id="5" format="pickle">gASV0QAAAAAAAAB9lCiMCG1ldGFkYXRhlH2UjBNzYXZlZFdpZGdldEdlb21ldHJ5lIwDc2lwlIwO
X3VucGlja2xlX3R5cGWUk5SMDFB5UXQ1LlF0Q29yZZSMClFCeXRlQXJyYXmUQ0IB2dDLAAMAAAAA
AwsAAAFgAAAEdAAAAnYAAAMMAAABhgAABHMAAAJ1AAAAAAAAAAAHgAAAAwwAAAGGAAAEcwAAAnWU
hZSHlFKUjA5zZXRfYnJlYWtwb2ludJSJjAZzdHJlYW2UjACUjAd2ZXJib3NllIl1Lg==
</properties>
		<properties node_id="6" format="pickle">gASV0QIAAAAAAAB9lCiMDWNhbGliX3NlY29uZHOUSxSMD2Nvb3Jkc19vdmVycmlkZZSMDSh1c2Ug
ZGVmYXVsdCmUjA5jb3JyX3RocmVzaG9sZJRHP+mZmZmZmZqMD2lnbm9yZV9jaGFubG9jc5SJjBBp
Z25vcmVkX3F1YW50aWxllEc/uZmZmZmZmowHaW5pdF9vbpRdlIwZa2VlcF91bmxvY2FsaXplZF9j
aGFubmVsc5SJjA9saW5lbm9pc2VfYXdhcmWUiIwQbWF4X2JhZF9jaGFubmVsc5RHP8MzMzMzMzOM
D21heF9icm9rZW5fdGltZZRHP9mZmZmZmZqMCG1ldGFkYXRhlH2UjAhtaW5fY29ycpRHP+AAAAAA
AACMD25vaXNlX3RocmVzaG9sZJRHQBAAAAAAAACMC251bV9zYW1wbGVzlEvIjBBwcm90ZWN0X2No
YW5uZWxzlF2UKIwCRjeUjANGQzWUjAJGOJSMA0ZDNpSMAkZ6lIwDQUZ6lGWMDHJlcmVmZXJlbmNl
ZJSJjBNzYXZlZFdpZGdldEdlb21ldHJ5lIwDc2lwlIwOX3VucGlja2xlX3R5cGWUk5SMDFB5UXQ1
LlF0Q29yZZSMClFCeXRlQXJyYXmUQ0IB2dDLAAMAAAAAAv8AAACNAAAFnQAAA0kAAAMAAAAAswAA
BZwAAANIAAAAAAAAAAAHgAAAAwAAAACzAAAFnAAAA0iUhZSHlFKUjA5zZXRfYnJlYWtwb2ludJSJ
jAtzdWJzZXRfc2l6ZZRHP8MzMzMzMzOMEHVzZV9jbGVhbl93aW5kb3eUiYwKd2luZG93X2xlbpRH
QBQAAAAAAACMFndpbmRvd19sZW5fY2xlYW53aW5kb3eURz/gAAAAAAAAjA53aW5kb3dfb3Zlcmxh
cJRHP+UeuFHrhR+MEXpzY29yZV90aHJlc2hvbGRzlF2UKEfADAAAAAAAAEsFZXUu
</properties>
		<properties node_id="7" format="pickle">gASVggEAAAAAAAB9lCiMFGFkZGl0aXZlX25vaXNlX3NjYWxllEcAAAAAAAAAAIwHYmFja2VuZJSM
BGtlZXCUjBBkZXNpcmVkX2NoYW5uZWxzlF2UjAhtZXRhZGF0YZR9lIwGbWluX2V2lIwNKHVzZSBk
ZWZhdWx0KZSMBG1vZGWUjBBzcGhlcmljYWwtc3BsaW5llIwHbW9udGFnZZSMAJSMDG1vbnRhZ2Vf
dHlwZZSMBGF1dG+UjAlwcmVjaXNpb26UjARrZWVwlIwIcmFuZHNlZWSUTTkwjBNzYXZlZFdpZGdl
dEdlb21ldHJ5lIwDc2lwlIwOX3VucGlja2xlX3R5cGWUk5SMDFB5UXQ1LlF0Q29yZZSMClFCeXRl
QXJyYXmUQ0IB2dDLAAMAAAAAAt8AAABvAAAEogAAA9cAAALfAAAAbwAABKIAAAPXAAAAAAAAAAAH
gAAAAt8AAABvAAAEogAAA9eUhZSHlFKUjA5zZXRfYnJlYWtwb2ludJSJjAd2ZXJib3NllIl1Lg==
</properties>
		<properties node_id="8" format="pickle">gASVzAIAAAAAAAB9lCiMAWGUjA0odXNlIGRlZmF1bHQplIwBYpRoAowKYmxvY2tfc2l6ZZRoAowN
Y2FsaWJfc2Vjb25kc5RLLYwGY3V0b2ZmlEdAHgAAAAAAAIwPZW1pdF9jYWxpYl9kYXRhlIiMB2lu
aXRfb26UXZSMCWxvb2thaGVhZJRoAowQbWF4X2JhZF9jaGFubmVsc5RHP8mZmZmZmZqMCG1heF9k
aW1zlEcAAAAAAAAAAIwUbWF4X2Ryb3BvdXRfZnJhY3Rpb26URz+5mZmZmZmajAdtYXhfbWVtlE0A
AYwIbWV0YWRhdGGUfZSMEm1pbl9jbGVhbl9mcmFjdGlvbpRHP9AAAAAAAACMFW1pbl9yZXF1aXJl
ZF9jaGFubmVsc5RLAowNcHJlc2VydmVfYmFuZJRoAowKcmllbWFubmlhbpSJjBNzYXZlZFdpZGdl
dEdlb21ldHJ5lIwDc2lwlIwOX3VucGlja2xlX3R5cGWUk5SMDFB5UXQ1LlF0Q29yZZSMClFCeXRl
QXJyYXmUQ0IB2dDLAAMAAAAAAv8AAACUAAAE5QAAA/cAAAMAAAAAugAABOQAAAP2AAAAAAAAAAAH
gAAAAwAAAAC6AAAE5AAAA/aUhZSHlFKUjA5zZXRfYnJlYWtwb2ludJSJjA1zdGRkZXZfY3V0b2Zm
lEsUjAlzdGVwX3NpemWURz/JmZmZmZmajBB1c2VfY2xlYW5fd2luZG93lImMCnVzZV9sZWdhY3mU
iYwWd2luZG93X2xlbl9jbGVhbndpbmRvd5RHP+AAAAAAAACMDXdpbmRvd19sZW5ndGiURz/gAAAA
AAAAjA53aW5kb3dfb3ZlcmxhcJRHP+UeuFHrhR+MGndpbmRvd19vdmVybGFwX2NsZWFud2luZG93
lEc/5R64UeuFH4wRenNjb3JlX3RocmVzaG9sZHOUXZQoSvv///9LB2V1Lg==
</properties>
		<properties node_id="9" format="pickle">gASVXAEAAAAAAAB9lCiMEWtlZXBfbWFya2VyX2NodW5rlImMDm1heF9nYXBfbGVuZ3RolEc/yZmZ
mZmZmowIbWV0YWRhdGGUfZSMD29ubGluZV9lcG9jaGluZ5SMB3NsaWRpbmeUjA1zYW1wbGVfb2Zm
c2V0lEsAjBNzYXZlZFdpZGdldEdlb21ldHJ5lIwDc2lwlIwOX3VucGlja2xlX3R5cGWUk5SMDFB5
UXQ1LlF0Q29yZZSMClFCeXRlQXJyYXmUQ0IB2dDLAAMAAAAABHAAAADVAAAGNQAAA4QAAARxAAAA
+wAABjQAAAODAAAAAAAAAAAHgAAABHEAAAD7AAAGNAAAA4OUhZSHlFKUjA5zZWxlY3RfbWFya2Vy
c5SMDSh1c2UgZGVmYXVsdCmUjA5zZXRfYnJlYWtwb2ludJSJjAt0aW1lX2JvdW5kc5RdlChK////
/0sAZYwHdmVyYm9zZZSJdS4=
</properties>
		<properties node_id="10" format="pickle">gASVXQEAAAAAAAB9lCiMBGF4aXOUjAVzcGFjZZSMC2lnbm9yZV9uYW5zlImMB21hcHBpbmeUfZQo
jAdsZWZ0SUZHlF2UKIwCRjeUjANGQzWUZYwCRnqUXZSMAkZ6lGF1jAhtZXRhZGF0YZR9lIwJb3Bl
cmF0aW9ulIwHYXZlcmFnZZSME3NhdmVkV2lkZ2V0R2VvbWV0cnmUjANzaXCUjA5fdW5waWNrbGVf
dHlwZZSTlIwMUHlRdDUuUXRDb3JllIwKUUJ5dGVBcnJheZRDQgHZ0MsAAwAAAAADHwAAAOUAAASI
AAAC2wAAAyAAAAELAAAEhwAAAtoAAAAAAAAAAAeAAAADIAAAAQsAAASHAAAC2pSFlIeUUpSMDnNl
dF9icmVha3BvaW50lImMEXN1cHBvcnRfd2lsZGNhcmRzlImMB3ZlcmJvc2WUiYwKd3JpdGVfYmFj
a5SMC3JlcGxhY2UtYWxslHUu
</properties>
		<properties node_id="11" format="pickle">gASVHQEAAAAAAAB9lCiME2JhbmR3aWR0aF9mcmVxdWVuY3mURz/wAAAAAAAAjBFjZW50cmFsX2Zy
ZXF1ZW5jeZRHQBgAAAAAAACMCG1ldGFkYXRhlH2UjBNzYXZlZFdpZGdldEdlb21ldHJ5lIwDc2lw
lIwOX3VucGlja2xlX3R5cGWUk5SMDFB5UXQ1LlF0Q29yZZSMClFCeXRlQXJyYXmUQ0IB2dDLAAMA
AAAABLIAAAEkAAAGsQAAAvEAAASzAAABSgAABrAAAALwAAAAAAAAAAAHgAAABLMAAAFKAAAGsAAA
AvCUhZSHlFKUjAtzY2FsZV9yYW5nZZRdlChLBktGZYwOc2V0X2JyZWFrcG9pbnSUiYwHd2F2ZWxl
dJSMBG1vcmyUdS4=
</properties>
		<properties node_id="12" format="pickle">gASVaAEAAAAAAAB9lCiMBGF4aXOUjAR0aW1llIwGZGVzaWdulIwGYnV0dGVylIwLZnJlcXVlbmNp
ZXOUXZQoSzBLNGWMC2lnbm9yZV9uYW5zlImMCG1ldGFkYXRhlH2UjARtb2RllIwIYmFuZHN0b3CU
jBBvZmZsaW5lX2ZpbHRmaWx0lImMBW9yZGVylIwNKHVzZSBkZWZhdWx0KZSMCXBhc3NfbG9zc5RH
QAgAAAAAAACME3NhdmVkV2lkZ2V0R2VvbWV0cnmUjANzaXCUjA5fdW5waWNrbGVfdHlwZZSTlIwM
UHlRdDUuUXRDb3JllIwKUUJ5dGVBcnJheZRDQgHZ0MsAAwAAAAADCwAAAKMAAAR0AAADNAAAAwwA
AADJAAAEcwAAAzMAAAAAAAAAAAeAAAADDAAAAMkAAARzAAADM5SFlIeUUpSMDnNldF9icmVha3Bv
aW50lImMCnN0b3BfYXR0ZW6UR0BJAAAAAAAAdS4=
</properties>
		<properties node_id="13" format="pickle">gASVQQEAAAAAAAB9lCiMB2RldHJlbmSUjAhjb25zdGFudJSMCGZmdF9zaXpllIwNKHVzZSBkZWZh
dWx0KZSMD2ZsYXRfc3BhY2VfYXhpc5SJjAhtZXRhZGF0YZR9lIwIb25lc2lkZWSUiIwPb3Zlcmxh
cF9zYW1wbGVzlGgEjBNzYXZlZFdpZGdldEdlb21ldHJ5lIwDc2lwlIwOX3VucGlja2xlX3R5cGWU
k5SMDFB5UXQ1LlF0Q29yZZSMClFCeXRlQXJyYXmUQ0IB2dDLAAMAAAAAAwsAAADtAAAEdAAAAuoA
AAMMAAABEwAABHMAAALpAAAAAAAAAAAHgAAAAwwAAAETAAAEcwAAAumUhZSHlFKUjA9zZWdtZW50
X3NhbXBsZXOUSw+MDnNldF9icmVha3BvaW50lImMBndpbmRvd5SMBGhhbm6UdS4=
</properties>
		<properties node_id="14" format="pickle">gASVLQEAAAAAAAB9lCiME2FwcGx5X211bHRpcGxlX2F4ZXOUiYwfYXBwbHlfdGltZV9zZWxlY3Rp
b25fdG9fbWFya2Vyc5SJjARheGlzlIwJZnJlcXVlbmN5lIwIbWV0YWRhdGGUfZSME3NhdmVkV2lk
Z2V0R2VvbWV0cnmUjANzaXCUjA5fdW5waWNrbGVfdHlwZZSTlIwMUHlRdDUuUXRDb3JllIwKUUJ5
dGVBcnJheZRDQgHZ0MsAAwAAAAADDAAAATEAAARzAAAC6QAAAwwAAAExAAAEcwAAAukAAAAAAAAA
AAeAAAADDAAAATEAAARzAAAC6ZSFlIeUUpSMCXNlbGVjdGlvbpSMBjcuLi4xOZSMDnNldF9icmVh
a3BvaW50lImMBHVuaXSUjAdpbmRpY2VzlHUu
</properties>
		<properties node_id="15" format="pickle">gASVfQEAAAAAAAB9lCiMBGF4aXOUjAlmcmVxdWVuY3mUjA9heGlzX29jY3VycmVuY2WUSwCMB2Jh
Y2tlbmSUjARrZWVwlIwSZm9yY2VfZmVhdHVyZV9heGlzlImMC2lnbm9yZV9uYW5zlImMCWtlZXBf
YXhpc5SIjAhtZXRhZGF0YZR9lIwJcHJlY2lzaW9ulIwEa2VlcJSMBnJvYnVzdJSJjBVyb2J1c3Rf
ZXN0aW1hdG9yX3R5cGWUjAZtZWRpYW6UjBNzYXZlZFdpZGdldEdlb21ldHJ5lIwDc2lwlIwOX3Vu
cGlja2xlX3R5cGWUk5SMDFB5UXQ1LlF0Q29yZZSMClFCeXRlQXJyYXmUQ0IB2dDLAAMAAAAAAk8A
AACbAAADuAAAAxEAAAJQAAAAwQAAA7cAAAMQAAAAAAAAAAAHgAAAAlAAAADBAAADtwAAAxCUhZSH
lFKUjA5zZXRfYnJlYWtwb2ludJSJjA90cmltX3Byb3BvcnRpb26URz+5mZmZmZmadS4=
</properties>
		<properties node_id="16" format="pickle">gASV0wAAAAAAAAB9lCiMCGZpbGVuYW1llIwLUHJ1ZWJhMi5yZWOUjAhtZXRhZGF0YZR9lIwTc2F2
ZWRXaWRnZXRHZW9tZXRyeZSMA3NpcJSMDl91bnBpY2tsZV90eXBllJOUjAxQeVF0NS5RdENvcmWU
jApRQnl0ZUFycmF5lENCAdnQywADAAAAAAMLAAABbQAABHQAAAJqAAADDAAAAZMAAARzAAACaQAA
AAAAAAAAB4AAAAMMAAABkwAABHMAAAJplIWUh5RSlIwOc2V0X2JyZWFrcG9pbnSUiXUu
</properties>
		<properties node_id="17" format="pickle">gASVNwEAAAAAAAB9lCiME2FwcGx5X211bHRpcGxlX2F4ZXOUiYwfYXBwbHlfdGltZV9zZWxlY3Rp
b25fdG9fbWFya2Vyc5SJjARheGlzlIwFbmFtZWSUjAhtZXRhZGF0YZR9lIwTc2F2ZWRXaWRnZXRH
ZW9tZXRyeZSMA3NpcJSMDl91bnBpY2tsZV90eXBllJOUjAxQeVF0NS5RdENvcmWUjApRQnl0ZUFy
cmF5lENCAdnQywADAAAAAAMLAAABCwAABHQAAALMAAADDAAAATEAAARzAAACywAAAAAAAAAAB4AA
AAMMAAABMQAABHMAAALLlIWUh5RSlIwJc2VsZWN0aW9ulF2UjBRBY3RpQ2hhbXBfMC1yaWdodElG
R5RhjA5zZXRfYnJlYWtwb2ludJSJjAR1bml0lIwEYXV0b5R1Lg==
</properties>
		<properties node_id="18" format="pickle">gASVVgIAAAAAAAB9lCiMCWNodW5rX2xlbpRLAIwVaWdub3JlX3NpZ25hbF9jaGFuZ2VklImME2tl
ZXBfc2luZ2xldG9uX2F4ZXOUiYwMbWFya2VyX2ZpZWxklIwGTWFya2VylIwLbWFya2VyX25hbWWU
jBFPdXRTdHJlYW0tbWFya2Vyc5SMEG1hcmtlcl9zb3VyY2VfaWSUjACUjAxtYXhfYnVmZmVyZWSU
SzyMCG1ldGFkYXRhlH2UjBdudW1lcmljX2xhYmVsX3ByZWNpc2lvbpRLAYwYbnVtZXJpY19tYXJr
ZXJfcHJlY2lzaW9ulEsDjBdyZXNldF9pZl9sYWJlbHNfY2hhbmdlZJSJjBNzYXZlZFdpZGdldEdl
b21ldHJ5lIwDc2lwlIwOX3VucGlja2xlX3R5cGWUk5SMDFB5UXQ1LlF0Q29yZZSMClFCeXRlQXJy
YXmUQ0IB2dDLAAMAAAAAAwsAAACNAAAEdAAAA0kAAAMMAAAAswAABHMAAANIAAAAAAAAAAAHgAAA
AwwAAACzAAAEcwAAA0iUhZSHlFKUjAxzZW5kX21hcmtlcnOUiYwJc2VwYXJhdG9ylIwBLZSMDnNl
dF9icmVha3BvaW50lImMCXNvdXJjZV9pZJSMA0lGR5SMBXNyYXRllIwNKHVzZSBkZWZhdWx0KZSM
C3N0cmVhbV9uYW1llIwDSUZHlIwLc3RyZWFtX3R5cGWUjAljb2hlcmVuY2WUjBN1c2VfZGF0YV90
aW1lc3RhbXBzlIiMFnVzZV9udW1weV9vcHRpbWl6YXRpb26UiHUu
</properties>
		<properties node_id="19" format="pickle">gASVAwIAAAAAAAB9lCiMF2Fic29sdXRlX2luc3RhbmNlX3RpbWVzlIiMDWNsb3VkX2FjY291bnSU
jACUjAxjbG91ZF9idWNrZXSUaAOMEWNsb3VkX2NyZWRlbnRpYWxzlGgDjApjbG91ZF9ob3N0lIwH
RGVmYXVsdJSMDWNvbHVtbl9oZWFkZXKUiIwMZGVsZXRlX3BhcnRzlIiMCGZpbGVuYW1llIwQR3J1
cG8xMEplbmdhLmNzdpSMCG1ldGFkYXRhlH2UjAtvdXRwdXRfcm9vdJSMUUM6L1VzZXJzL21mb3J0
L0Rlc2t0b3AvQ0FSL1Byb3llY3Rvcy9JbnRlcmJyYWluIFN5bmNocm9uaXphdGlvbi9SZXN1bHRh
ZG9zL1RyaWFsc5SMC3JldHJpZXZhYmxllImME3NhdmVkV2lkZ2V0R2VvbWV0cnmUjANzaXCUjA5f
dW5waWNrbGVfdHlwZZSTlIwMUHlRdDUuUXRDb3JllIwKUUJ5dGVBcnJheZRDQgHZ0MsAAwAAAAAE
kAAAAMoAAAX3AAADVgAABJAAAADKAAAF9wAAA1YAAAAAAAAAAAeAAAAEkAAAAMoAAAX3AAADVpSF
lIeUUpSMDnNldF9icmVha3BvaW50lImMC3RpbWVfc3RhbXBzlIiMD3RpbWVzdGFtcF9sYWJlbJSM
CXRpbWVzdGFtcJR1Lg==
</properties>
		<properties node_id="20" format="pickle">gASVSAEAAAAAAAB9lCiMBGF4aXOUjAVuYW1lZJSMCGN1dF9wcm9wlEc/uZmZmZmZmowJZXN0aW1h
dG9ylIwEbWVhbpSMCG1ldGFkYXRhlH2UjA9yZWZlcmVuY2VfcmFuZ2WUXZSMAkZ6lGGMDnJlZmVy
ZW5jZV91bml0lIwFbmFtZXOUjBNzYXZlZFdpZGdldEdlb21ldHJ5lIwDc2lwlIwOX3VucGlja2xl
X3R5cGWUk5SMDFB5UXQ1LlF0Q29yZZSMClFCeXRlQXJyYXmUQ0IB2dDLAAMAAAAAAv0AAAEqAAAE
ggAAAtEAAAL9AAABKgAABIIAAALRAAAAAAAAAAAHgAAAAv0AAAEqAAAEggAAAtGUhZSHlFKUjA5z
ZXRfYnJlYWtwb2ludJSJjBZ1c2Vfc2VwYXJhdGVfcmVmZXJlbmNllImMB3ZlcmJvc2WUiHUu
</properties>
		<properties node_id="21" format="pickle">gASV4QAAAAAAAAB9lCiMCG1ldGFkYXRhlH2UjBFyZXBsYWNlX2lmX2V4aXN0c5SJjBNzYXZlZFdp
ZGdldEdlb21ldHJ5lIwDc2lwlIwOX3VucGlja2xlX3R5cGWUk5SMDFB5UXQ1LlF0Q29yZZSMClFC
eXRlQXJyYXmUQ0IB2dDLAAMAAAAAAwwAAAGHAAAEcwAAAnQAAAMMAAABhwAABHMAAAJ0AAAAAAAA
AAAHgAAAAwwAAAGHAAAEcwAAAnSUhZSHlFKUjA5zZXRfYnJlYWtwb2ludJSJjAdzb3J0aW5nlIwF
aW5wdXSUdS4=
</properties>
		<properties node_id="22" format="pickle">gASVMgEAAAAAAAB9lCiMDGJ1ZmZlcl9kZWxheZRHQAAAAAAAAACMEGRlc2lyZWRfaGVhZHJvb22U
R0AUAAAAAAAAjAhtZXRhZGF0YZR9lIwMbWluX2hlYWRyb29tlEdAAAAAAAAAAIwTc2F2ZWRXaWRn
ZXRHZW9tZXRyeZSMA3NpcJSMDl91bnBpY2tsZV90eXBllJOUjAxQeVF0NS5RdENvcmWUjApRQnl0
ZUFycmF5lENCAdnQywADAAAAAAMMAAABMQAABHMAAALKAAADDAAAATEAAARzAAACygAAAAAAAAAA
B4AAAAMMAAABMQAABHMAAALKlIWUh5RSlIwOc2V0X2JyZWFrcG9pbnSUiYwFc3JhdGWUS32MC3N0
cmVhbV9uYW1llIwDZWVnlIwJdmVyYm9zaXR5lEsBdS4=
</properties>
		<properties node_id="23" format="pickle">gASVKwEAAAAAAAB9lCiME2FwcGx5X211bHRpcGxlX2F4ZXOUiYwfYXBwbHlfdGltZV9zZWxlY3Rp
b25fdG9fbWFya2Vyc5SJjARheGlzlIwFbmFtZWSUjAhtZXRhZGF0YZR9lIwTc2F2ZWRXaWRnZXRH
ZW9tZXRyeZSMA3NpcJSMDl91bnBpY2tsZV90eXBllJOUjAxQeVF0NS5RdENvcmWUjApRQnl0ZUFy
cmF5lENCAdnQywADAAAAAAS0AAABMQAABh0AAALyAAAEtQAAAVcAAAYcAAAC8QAAAAAAAAAAB4AA
AAS1AAABVwAABhwAAALxlIWUh5RSlIwJc2VsZWN0aW9ulF2UjAdsZWZ0SUZHlGGMDnNldF9icmVh
a3BvaW50lImMBHVuaXSUjAVuYW1lc5R1Lg==
</properties>
		<properties node_id="24" format="pickle">gASVLAEAAAAAAAB9lCiME2FwcGx5X211bHRpcGxlX2F4ZXOUiYwfYXBwbHlfdGltZV9zZWxlY3Rp
b25fdG9fbWFya2Vyc5SJjARheGlzlIwFbmFtZWSUjAhtZXRhZGF0YZR9lIwTc2F2ZWRXaWRnZXRH
ZW9tZXRyeZSMA3NpcJSMDl91bnBpY2tsZV90eXBllJOUjAxQeVF0NS5RdENvcmWUjApRQnl0ZUFy
cmF5lENCAdnQywADAAAAAATWAAAA9AAABj8AAAK1AAAE1wAAARoAAAY+AAACtAAAAAAAAAAAB4AA
AATXAAABGgAABj4AAAK0lIWUh5RSlIwJc2VsZWN0aW9ulF2UjAhyaWdodElGR5RhjA5zZXRfYnJl
YWtwb2ludJSJjAR1bml0lIwFbmFtZXOUdS4=
</properties>
		<properties node_id="25" format="pickle">gASVYAEAAAAAAAB9lCiMBGF4aXOUjAVzcGFjZZSMC2lnbm9yZV9uYW5zlImMB21hcHBpbmeUfZQo
jAhyaWdodElGR5RdlCiMAkY4lIwDRkM2lGWMA0FGepRdlIwDQUZ6lGF1jAhtZXRhZGF0YZR9lIwJ
b3BlcmF0aW9ulIwHYXZlcmFnZZSME3NhdmVkV2lkZ2V0R2VvbWV0cnmUjANzaXCUjA5fdW5waWNr
bGVfdHlwZZSTlIwMUHlRdDUuUXRDb3JllIwKUUJ5dGVBcnJheZRDQgHZ0MsAAwAAAAABvAAAAQUA
AAMjAAAC1AAAAbwAAAEFAAADIwAAAtQAAAAAAAAAAAeAAAABvAAAAQUAAAMjAAAC1JSFlIeUUpSM
DnNldF9icmVha3BvaW50lImMEXN1cHBvcnRfd2lsZGNhcmRzlImMB3ZlcmJvc2WUiYwKd3JpdGVf
YmFja5SMC3JlcGxhY2UtYWxslHUu
</properties>
		<properties node_id="26" format="pickle">gASVSQEAAAAAAAB9lCiMBGF4aXOUjAVuYW1lZJSMCGN1dF9wcm9wlEc/uZmZmZmZmowJZXN0aW1h
dG9ylIwEbWVhbpSMCG1ldGFkYXRhlH2UjA9yZWZlcmVuY2VfcmFuZ2WUXZSMA0FGepRhjA5yZWZl
cmVuY2VfdW5pdJSMBW5hbWVzlIwTc2F2ZWRXaWRnZXRHZW9tZXRyeZSMA3NpcJSMDl91bnBpY2ts
ZV90eXBllJOUjAxQeVF0NS5RdENvcmWUjApRQnl0ZUFycmF5lENCAdnQywADAAAAAASVAAAA2AAA
BhwAAAKmAAAElgAAAP4AAAYbAAACpQAAAAAAAAAAB4AAAASWAAAA/gAABhsAAAKllIWUh5RSlIwO
c2V0X2JyZWFrcG9pbnSUiYwWdXNlX3NlcGFyYXRlX3JlZmVyZW5jZZSJjAd2ZXJib3NllIh1Lg==
</properties>
	</node_properties>
	<patch>{"description": {"description": "This pipeline preprocesses and cleans the EEG, then computes the average power across channels in a moving window for a specific frequency band, and then both plots it and sends it out over the network for pickup by another application (i.e., a game) \n\nIt also demonstrates a way of compting spectral power for multiple bands at once.", "license": "", "name": "Preprocess EEG Compute Bandpower", "status": "(unspecified)", "url": "", "version": "0.0.0"}, "edges": [["node7", "data", "node9", "data"], ["node5", "data", "node7", "data"], ["node5", "data", "node6", "data"], ["node9", "data", "node8", "data"], ["node6", "channel_names", "node8", "desired_channels"], ["node4", "data", "node5", "data"], ["node13", "data", "node3", "data"], ["node2", "data", "node13", "data"], ["node15", "data", "node16", "data"], ["node18", "data", "node19", "data"], ["node18", "data", "node20", "data"], ["node22", "outdata", "node23", "data"], ["node21", "data", "node24", "data"], ["node16", "data", "node18", "data"], ["node27", "data", "node25", "data"], ["node11", "data", "node21", "data"], ["node26", "data", "node27", "data"], ["node10", "data", "node12", "data"], ["node12", "data", "node14", "data"], ["node23", "data", "node10", "data"], ["node14", "data", "node15", "data"], ["node3", "data", "node4", "data"], ["node8", "data", "node11", "data"], ["node8", "data", "node26", "data"], ["node24", "data", "node22", "data1"], ["node25", "data", "node22", "data2"], ["node1", "data", "node2", "data"]], "nodes": {"node1": {"class": "LSLInput", "module": "neuropype.nodes.network.LSLInput", "params": {"channel_names": {"customized": true, "type": "ListPort", "value": ["F7", "AF7", "FP1", "AF3", "F5", "F3", "F1", "Fz", "FT7", "FC5", "FC3", "FC1", "T7", "CP5", "C3", "C1", "F8", "AF8", "FP2", "AF4", "F6", "F4", "F2", "AFz", "FT8", "FC6", "FC4", "FC2", "T8", "CP6", "C4", "C2"]}, "data_dtype": {"customized": false, "type": "EnumPort", "value": "float64"}, "diagnostics": {"customized": false, "type": "BoolPort", "value": false}, "exclude_desc_fields": {"customized": false, "type": "ListPort", "value": []}, "localhost_only": {"customized": false, "type": "BoolPort", "value": false}, "marker_query": {"customized": false, "type": "StringPort", "value": ""}, "max_blocklen": {"customized": false, "type": "IntPort", "value": 1024}, "max_buflen": {"customized": false, "type": "IntPort", "value": 30}, "max_chunklen": {"customized": false, "type": "IntPort", "value": 0}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "nominal_rate": {"customized": false, "type": "FloatPort", "value": null}, "omit_desc": {"customized": false, "type": "BoolPort", "value": false}, "prealloc_buffer": {"customized": false, "type": "BoolPort", "value": true}, "proc_clocksync": {"customized": false, "type": "BoolPort", "value": true}, "proc_dejitter": {"customized": false, "type": "BoolPort", "value": false}, "proc_monotonize": {"customized": false, "type": "BoolPort", "value": false}, "proc_threadsafe": {"customized": false, "type": "BoolPort", "value": false}, "query": {"customized": false, "type": "StringPort", "value": "type='EEG'"}, "recover": {"customized": false, "type": "BoolPort", "value": true}, "resolve_minimum_time": {"customized": false, "type": "FloatPort", "value": 0.5}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "use_streamnames": {"customized": false, "type": "BoolPort", "value": false}}, "uuid": "ddde8ae0-2067-408d-91af-6ac6cfa67be5"}, "node10": {"class": "Segmentation", "module": "neuropype.nodes.formatting.Segmentation", "params": {"keep_marker_chunk": {"customized": false, "type": "BoolPort", "value": false}, "max_gap_length": {"customized": false, "type": "FloatPort", "value": 0.2}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "online_epoching": {"customized": true, "type": "EnumPort", "value": "sliding"}, "sample_offset": {"customized": false, "type": "IntPort", "value": 0}, "select_markers": {"customized": false, "type": "ListPort", "value": null}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "time_bounds": {"customized": true, "type": "ListPort", "value": [-1, 0]}, "verbose": {"customized": false, "type": "BoolPort", "value": false}}, "uuid": "0d2860e7-a8fc-4ab0-97ae-3f7ef37e9122"}, "node11": {"class": "CombineChannels", "module": "neuropype.nodes.signal_processing.CombineChannels", "params": {"axis": {"customized": false, "type": "ComboPort", "value": "space"}, "ignore_nans": {"customized": false, "type": "BoolPort", "value": false}, "mapping": {"customized": true, "type": "Port", "value": {"Fz": ["Fz"], "leftIFG": ["F7", "FC5"]}}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "operation": {"customized": false, "type": "EnumPort", "value": "average"}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "support_wildcards": {"customized": false, "type": "BoolPort", "value": false}, "verbose": {"customized": false, "type": "BoolPort", "value": false}, "write_back": {"customized": true, "type": "EnumPort", "value": "replace-all"}}, "uuid": "f4f339af-e1e5-40d9-8f0b-356f9c07290b"}, "node12": {"class": "ContinuousWaveletTransform", "module": "neuropype.nodes.spectral.ContinuousWaveletTransform", "params": {"bandwidth_frequency": {"customized": false, "type": "FloatPort", "value": 1.0}, "central_frequency": {"customized": true, "type": "FloatPort", "value": 6.0}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "scale_range": {"customized": true, "type": "ListPort", "value": [6, 70]}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "wavelet": {"customized": true, "type": "EnumPort", "value": "morl"}}, "uuid": "354fe84d-cba2-42f2-845e-4eb0be3a30a7"}, "node13": {"class": "IIRFilter", "module": "neuropype.nodes.signal_processing.IIRFilter", "params": {"axis": {"customized": false, "type": "ComboPort", "value": "time"}, "design": {"customized": false, "type": "EnumPort", "value": "butter"}, "frequencies": {"customized": true, "type": "ListPort", "value": [48, 52]}, "ignore_nans": {"customized": false, "type": "BoolPort", "value": false}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "mode": {"customized": true, "type": "EnumPort", "value": "bandstop"}, "offline_filtfilt": {"customized": false, "type": "BoolPort", "value": false}, "order": {"customized": false, "type": "IntPort", "value": null}, "pass_loss": {"customized": false, "type": "FloatPort", "value": 3.0}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "stop_atten": {"customized": false, "type": "FloatPort", "value": 50.0}}, "uuid": "e578edcc-d5b2-4ae2-88ca-6a23511441db"}, "node14": {"class": "Coherence", "module": "neuropype.nodes.spectral.Coherence", "params": {"detrend": {"customized": false, "type": "EnumPort", "value": "constant"}, "fft_size": {"customized": false, "type": "IntPort", "value": null}, "flat_space_axis": {"customized": false, "type": "BoolPort", "value": false}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "onesided": {"customized": false, "type": "BoolPort", "value": true}, "overlap_samples": {"customized": false, "type": "FloatPort", "value": null}, "segment_samples": {"customized": true, "type": "IntPort", "value": 15}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "window": {"customized": false, "type": "EnumPort", "value": "hann"}}, "uuid": "b1e607ed-5be4-49b3-a8dc-e43f8f1c1c4e"}, "node15": {"class": "SelectRange", "module": "neuropype.nodes.tensor_math.SelectRange", "params": {"apply_multiple_axes": {"customized": false, "type": "BoolPort", "value": false}, "apply_time_selection_to_markers": {"customized": false, "type": "BoolPort", "value": false}, "axis": {"customized": true, "type": "ComboPort", "value": "frequency"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "selection": {"customized": true, "type": "Port", "value": "7...19"}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "unit": {"customized": false, "type": "EnumPort", "value": "indices"}}, "uuid": "f134a084-140c-4e7d-9e78-27e0a4c27618"}, "node16": {"class": "Mean", "module": "neuropype.nodes.statistics.Mean", "params": {"axis": {"customized": true, "type": "ComboPort", "value": "frequency"}, "axis_occurrence": {"customized": false, "type": "IntPort", "value": 0}, "backend": {"customized": false, "type": "EnumPort", "value": "keep"}, "force_feature_axis": {"customized": false, "type": "BoolPort", "value": false}, "ignore_nans": {"customized": false, "type": "BoolPort", "value": false}, "keep_axis": {"customized": false, "type": "BoolPort", "value": true}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "precision": {"customized": false, "type": "EnumPort", "value": "keep"}, "robust": {"customized": false, "type": "BoolPort", "value": false}, "robust_estimator_type": {"customized": false, "type": "EnumPort", "value": "median"}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "trim_proportion": {"customized": false, "type": "FloatPort", "value": 0.1}}, "uuid": "158b7c87-5162-4de7-9380-c1fd3946462d"}, "node17": {"class": "PlayBackREC", "module": "neuropype.nodes.file_system.PlayBackREC", "params": {"filename": {"customized": true, "type": "StringPort", "value": "Prueba2.rec"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}}, "uuid": "3c57e364-a9b7-4c1d-acca-1cdb385958a5"}, "node18": {"class": "SelectRange", "module": "neuropype.nodes.tensor_math.SelectRange", "params": {"apply_multiple_axes": {"customized": false, "type": "BoolPort", "value": false}, "apply_time_selection_to_markers": {"customized": false, "type": "BoolPort", "value": false}, "axis": {"customized": true, "type": "ComboPort", "value": "named"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "selection": {"customized": true, "type": "Port", "value": ["ActiChamp_0-rightIFG"]}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "unit": {"customized": true, "type": "EnumPort", "value": "auto"}}, "uuid": "315ca1a0-1952-4929-9e27-2ad691e2b917"}, "node19": {"class": "LSLOutput", "module": "neuropype.nodes.network.LSLOutput", "params": {"chunk_len": {"customized": false, "type": "IntPort", "value": 0}, "ignore_signal_changed": {"customized": false, "type": "BoolPort", "value": false}, "keep_singleton_axes": {"customized": false, "type": "BoolPort", "value": false}, "marker_field": {"customized": false, "type": "StringPort", "value": "Marker"}, "marker_name": {"customized": false, "type": "StringPort", "value": "OutStream-markers"}, "marker_source_id": {"customized": false, "type": "StringPort", "value": ""}, "max_buffered": {"customized": false, "type": "IntPort", "value": 60}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "numeric_label_precision": {"customized": false, "type": "IntPort", "value": 1}, "numeric_marker_precision": {"customized": false, "type": "IntPort", "value": 3}, "reset_if_labels_changed": {"customized": false, "type": "BoolPort", "value": false}, "send_markers": {"customized": false, "type": "BoolPort", "value": false}, "separator": {"customized": false, "type": "StringPort", "value": "-"}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "source_id": {"customized": true, "type": "StringPort", "value": "IFG"}, "srate": {"customized": false, "type": "FloatPort", "value": null}, "stream_name": {"customized": true, "type": "StringPort", "value": "IFG"}, "stream_type": {"customized": true, "type": "StringPort", "value": "coherence"}, "use_data_timestamps": {"customized": false, "type": "BoolPort", "value": true}, "use_numpy_optimization": {"customized": false, "type": "BoolPort", "value": true}}, "uuid": "db82e902-af09-47a5-8a64-44d9637b49d5"}, "node2": {"class": "DejitterTimestamps", "module": "neuropype.nodes.utilities.DejitterTimestamps", "params": {"force_monotonic": {"customized": false, "type": "BoolPort", "value": true}, "forget_halftime": {"customized": false, "type": "FloatPort", "value": 90.0}, "max_updaterate": {"customized": false, "type": "IntPort", "value": 500}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "warmup_samples": {"customized": false, "type": "IntPort", "value": -1}}, "uuid": "9b4ed036-bd52-431d-8e63-c5ffa9945574"}, "node20": {"class": "RecordToCSV", "module": "neuropype.nodes.file_system.RecordToCSV", "params": {"absolute_instance_times": {"customized": false, "type": "BoolPort", "value": true}, "cloud_account": {"customized": false, "type": "StringPort", "value": ""}, "cloud_bucket": {"customized": false, "type": "StringPort", "value": ""}, "cloud_credentials": {"customized": false, "type": "StringPort", "value": ""}, "cloud_host": {"customized": false, "type": "EnumPort", "value": "Default"}, "column_header": {"customized": false, "type": "BoolPort", "value": true}, "delete_parts": {"customized": false, "type": "BoolPort", "value": true}, "filename": {"customized": true, "type": "StringPort", "value": "Grupo10Jenga.csv"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "output_root": {"customized": true, "type": "StringPort", "value": "C:/Users/mfort/Desktop/CAR/Proyectos/Interbrain Synchronization/Resultados/Trials"}, "retrievable": {"customized": false, "type": "BoolPort", "value": false}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "time_stamps": {"customized": false, "type": "BoolPort", "value": true}, "timestamp_label": {"customized": false, "type": "StringPort", "value": "timestamp"}}, "uuid": "c9e258f6-acbf-4588-a62d-cd91348498c1"}, "node21": {"class": "Rereferencing", "module": "neuropype.nodes.signal_processing.Rereferencing", "params": {"axis": {"customized": true, "type": "ComboPort", "value": "named"}, "cut_prop": {"customized": false, "type": "FloatPort", "value": 0.1}, "estimator": {"customized": false, "type": "EnumPort", "value": "mean"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "reference_range": {"customized": true, "type": "Port", "value": ["Fz"]}, "reference_unit": {"customized": true, "type": "EnumPort", "value": "names"}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "use_separate_reference": {"customized": false, "type": "BoolPort", "value": false}, "verbose": {"customized": false, "type": "BoolPort", "value": true}}, "uuid": "05f4cc05-662c-47ce-b387-eaf7b7a77fb4"}, "node22": {"class": "MergeStreams", "module": "neuropype.nodes.formatting.MergeStreams", "params": {"metadata": {"customized": false, "type": "DictPort", "value": {}}, "replace_if_exists": {"customized": false, "type": "BoolPort", "value": false}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "sorting": {"customized": false, "type": "EnumPort", "value": "input"}}, "uuid": "32998a1d-b5c7-44ae-8521-cb33b7aeb0de"}, "node23": {"class": "FuseStreams", "module": "neuropype.nodes.formatting.FuseStreams", "params": {"buffer_delay": {"customized": false, "type": "FloatPort", "value": 2.0}, "desired_headroom": {"customized": false, "type": "FloatPort", "value": 5.0}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "min_headroom": {"customized": false, "type": "FloatPort", "value": 2.0}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "srate": {"customized": false, "type": "IntPort", "value": 125}, "stream_name": {"customized": false, "type": "StringPort", "value": "eeg"}, "verbosity": {"customized": false, "type": "IntPort", "value": 1}}, "uuid": "769078bc-0c19-4db0-8324-74ce51141530"}, "node24": {"class": "SelectRange", "module": "neuropype.nodes.tensor_math.SelectRange", "params": {"apply_multiple_axes": {"customized": false, "type": "BoolPort", "value": false}, "apply_time_selection_to_markers": {"customized": false, "type": "BoolPort", "value": false}, "axis": {"customized": true, "type": "ComboPort", "value": "named"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "selection": {"customized": true, "type": "Port", "value": ["leftIFG"]}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "unit": {"customized": true, "type": "EnumPort", "value": "names"}}, "uuid": "d5a364a5-881c-4b5b-a69e-3e4756c892af"}, "node25": {"class": "SelectRange", "module": "neuropype.nodes.tensor_math.SelectRange", "params": {"apply_multiple_axes": {"customized": false, "type": "BoolPort", "value": false}, "apply_time_selection_to_markers": {"customized": false, "type": "BoolPort", "value": false}, "axis": {"customized": true, "type": "ComboPort", "value": "named"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "selection": {"customized": true, "type": "Port", "value": ["rightIFG"]}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "unit": {"customized": true, "type": "EnumPort", "value": "names"}}, "uuid": "b9bac4d2-2d22-4254-a876-78f9e0c0bf9f"}, "node26": {"class": "CombineChannels", "module": "neuropype.nodes.signal_processing.CombineChannels", "params": {"axis": {"customized": false, "type": "ComboPort", "value": "space"}, "ignore_nans": {"customized": false, "type": "BoolPort", "value": false}, "mapping": {"customized": true, "type": "Port", "value": {"AFz": ["AFz"], "rightIFG": ["F8", "FC6"]}}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "operation": {"customized": false, "type": "EnumPort", "value": "average"}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "support_wildcards": {"customized": false, "type": "BoolPort", "value": false}, "verbose": {"customized": false, "type": "BoolPort", "value": false}, "write_back": {"customized": true, "type": "EnumPort", "value": "replace-all"}}, "uuid": "deb97ab5-8239-4fab-84a3-9cca55706f45"}, "node27": {"class": "Rereferencing", "module": "neuropype.nodes.signal_processing.Rereferencing", "params": {"axis": {"customized": true, "type": "ComboPort", "value": "named"}, "cut_prop": {"customized": false, "type": "FloatPort", "value": 0.1}, "estimator": {"customized": false, "type": "EnumPort", "value": "mean"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "reference_range": {"customized": true, "type": "Port", "value": ["AFz"]}, "reference_unit": {"customized": true, "type": "EnumPort", "value": "names"}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "use_separate_reference": {"customized": false, "type": "BoolPort", "value": false}, "verbose": {"customized": false, "type": "BoolPort", "value": true}}, "uuid": "02098fe1-c1c5-487b-9b7c-53bc31f6e772"}, "node3": {"class": "FIRFilter", "module": "neuropype.nodes.signal_processing.FIRFilter", "params": {"antisymmetric": {"customized": false, "type": "BoolPort", "value": false}, "axis": {"customized": false, "type": "ComboPort", "value": "time"}, "convolution_method": {"customized": false, "type": "EnumPort", "value": "standard"}, "cut_preringing": {"customized": false, "type": "BoolPort", "value": false}, "direction": {"customized": false, "type": "EnumPort", "value": "forward"}, "frequencies": {"customized": true, "type": "ListPort", "value": [3.0, 3.5, 30, 35]}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "minimum_phase": {"customized": false, "type": "BoolPort", "value": true}, "mode": {"customized": false, "type": "EnumPort", "value": "bandpass"}, "order": {"customized": false, "type": "IntPort", "value": null}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "stop_atten": {"customized": false, "type": "FloatPort", "value": 50.0}}, "uuid": "87872058-9fc4-4fde-aa1a-122b3111f6f1"}, "node4": {"class": "AssignChannelLocations", "module": "neuropype.nodes.source_localization.AssignChannelLocations", "params": {"force_override": {"customized": false, "type": "BoolPort", "value": true}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "montage": {"customized": false, "type": "StringPort", "value": ""}, "montage_type": {"customized": false, "type": "EnumPort", "value": "auto"}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}}, "uuid": "b23007f3-c00e-443a-bd2e-eea6c4b7861f"}, "node5": {"class": "RemoveUnlocalizedChannels", "module": "neuropype.nodes.source_localization.RemoveUnlocalizedChannels", "params": {"metadata": {"customized": false, "type": "DictPort", "value": {}}, "protect_channels": {"customized": false, "type": "ListPort", "value": []}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}}, "uuid": "da45c1be-73e0-4a87-a3c3-20406007418e"}, "node6": {"class": "ExtractChannels", "module": "neuropype.nodes.utilities.ExtractChannels", "params": {"metadata": {"customized": false, "type": "DictPort", "value": {}}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "stream": {"customized": false, "type": "StringPort", "value": ""}, "verbose": {"customized": false, "type": "BoolPort", "value": false}}, "uuid": "011f6889-a743-4d17-bdeb-fec4c8b19353"}, "node7": {"class": "BadChannelRemoval", "module": "neuropype.nodes.neural.BadChannelRemoval", "params": {"calib_seconds": {"customized": false, "type": "IntPort", "value": 20}, "coords_override": {"customized": false, "type": "FloatPort", "value": null}, "corr_threshold": {"customized": false, "type": "FloatPort", "value": 0.8}, "ignore_chanlocs": {"customized": false, "type": "BoolPort", "value": false}, "ignored_quantile": {"customized": false, "type": "FloatPort", "value": 0.1}, "init_on": {"customized": false, "type": "ListPort", "value": []}, "keep_unlocalized_channels": {"customized": false, "type": "BoolPort", "value": false}, "linenoise_aware": {"customized": false, "type": "BoolPort", "value": true}, "max_bad_channels": {"customized": false, "type": "FloatPort", "value": 0.15}, "max_broken_time": {"customized": false, "type": "FloatPort", "value": 0.4}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "min_corr": {"customized": false, "type": "FloatPort", "value": 0.5}, "noise_threshold": {"customized": false, "type": "FloatPort", "value": 4.0}, "num_samples": {"customized": false, "type": "IntPort", "value": 200}, "protect_channels": {"customized": true, "type": "ListPort", "value": ["F7", "FC5", "F8", "FC6", "Fz", "AFz"]}, "rereferenced": {"customized": false, "type": "BoolPort", "value": false}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "subset_size": {"customized": false, "type": "FloatPort", "value": 0.15}, "use_clean_window": {"customized": false, "type": "BoolPort", "value": false}, "window_len": {"customized": false, "type": "FloatPort", "value": 5.0}, "window_len_cleanwindow": {"customized": false, "type": "FloatPort", "value": 0.5}, "window_overlap": {"customized": false, "type": "FloatPort", "value": 0.66}, "zscore_thresholds": {"customized": false, "type": "ListPort", "value": [-3.5, 5]}}, "uuid": "6e5e379b-a866-458e-b0ee-1e99f682f32b"}, "node8": {"class": "InterpolateMissingChannels", "module": "neuropype.nodes.neural.InterpolateMissingChannels", "params": {"additive_noise_scale": {"customized": false, "type": "FloatPort", "value": 0.0}, "backend": {"customized": false, "type": "EnumPort", "value": "keep"}, "desired_channels": {"customized": true, "type": "ListPort", "value": ["F7", "AF7", "FP1", "AF3", "F5", "F3", "F1", "Fz", "FT7", "FC5", "FC3", "FC1", "T7", "CP5", "C3", "C1", "F8", "AF8", "FP2", "AF4", "F6", "F4", "F2", "AFz", "FT8", "FC6", "FC4", "FC2", "T8", "CP6", "C4", "C2"]}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "min_ev": {"customized": false, "type": "FloatPort", "value": null}, "mode": {"customized": false, "type": "EnumPort", "value": "spherical-spline"}, "montage": {"customized": false, "type": "StringPort", "value": ""}, "montage_type": {"customized": false, "type": "EnumPort", "value": "auto"}, "precision": {"customized": false, "type": "EnumPort", "value": "keep"}, "randseed": {"customized": false, "type": "IntPort", "value": 12345}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "verbose": {"customized": false, "type": "BoolPort", "value": false}}, "uuid": "d46625a7-a3f4-4bea-a676-b18b6f200cad"}, "node9": {"class": "ArtifactRemoval", "module": "neuropype.nodes.neural.ArtifactRemoval", "params": {"a": {"customized": false, "type": "Port", "value": null}, "b": {"customized": false, "type": "Port", "value": null}, "block_size": {"customized": false, "type": "IntPort", "value": null}, "calib_seconds": {"customized": false, "type": "IntPort", "value": 45}, "cutoff": {"customized": false, "type": "FloatPort", "value": 7.5}, "emit_calib_data": {"customized": false, "type": "BoolPort", "value": true}, "init_on": {"customized": false, "type": "ListPort", "value": []}, "lookahead": {"customized": false, "type": "Port", "value": null}, "max_bad_channels": {"customized": false, "type": "FloatPort", "value": 0.2}, "max_dims": {"customized": false, "type": "FloatPort", "value": 0.0}, "max_dropout_fraction": {"customized": false, "type": "FloatPort", "value": 0.1}, "max_mem": {"customized": false, "type": "Port", "value": 256}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "min_clean_fraction": {"customized": false, "type": "FloatPort", "value": 0.25}, "min_required_channels": {"customized": false, "type": "IntPort", "value": 2}, "preserve_band": {"customized": false, "type": "DictPort", "value": null}, "riemannian": {"customized": false, "type": "BoolPort", "value": false}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "stddev_cutoff": {"customized": false, "type": "IntPort", "value": 20}, "step_size": {"customized": false, "type": "FloatPort", "value": 0.2}, "use_clean_window": {"customized": true, "type": "BoolPort", "value": false}, "use_legacy": {"customized": false, "type": "BoolPort", "value": false}, "window_len_cleanwindow": {"customized": false, "type": "FloatPort", "value": 0.5}, "window_length": {"customized": false, "type": "FloatPort", "value": 0.5}, "window_overlap": {"customized": false, "type": "FloatPort", "value": 0.66}, "window_overlap_cleanwindow": {"customized": false, "type": "FloatPort", "value": 0.66}, "zscore_thresholds": {"customized": false, "type": "ListPort", "value": [-5, 7]}}, "uuid": "5e929147-ef80-456b-b468-de9611e0eb22"}}, "version": 1.1}</patch>
</scheme>
