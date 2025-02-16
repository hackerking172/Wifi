import qrcode

def generate_ip_qr(ip_address):
    """
    Generates a QR code for a WiFi router's IP address.
    
    :param ip_address: The router's IP address (e.g., "192.168.1.128")
    """
    # Generate QR Code
    qr = qrcode.QRCode(box_size=10, border=5)
    qr.add_data(f"http://{ip_address}")
    qr.make(fit=True)

    # Create and save the QR image
    img = qr.make_image(fill="black", back_color="white")
    img.show()  # Display the QR code
    img.save("wifi_ip_qr.png")  # Save as a file

# Example Usage
generate_ip_qr("192.168.1.128")  # Replace with your router's IP