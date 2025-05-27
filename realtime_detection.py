from scapy.all import sniff
from utils import extract_features_from_packet, predict_threat

def process_packet(packet):
    try:
        features = extract_features_from_packet(packet)
        threat_type = predict_threat(features)

        if threat_type != 'Normal':
            print(f"[ALERT] 🚨 Threat Detected: {threat_type}")
        else:
            print("✅ Normal traffic.")
    except Exception as e:
        print(f"[ERROR] Failed to process packet: {e}")

if __name__ == "__main__":
    print("🔍 Starting real-time packet monitoring... Press Ctrl+C to stop.")
    sniff(prn=process_packet, store=False)
