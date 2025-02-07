from kubernetes import client, config, watch

# Load Kubernetes configuration
config.load_incluster_config()  # Use config.load_kube_config() for local testing

# Initialize API client
api = client.CustomObjectsApi()

# Watch for Widget events
w = watch.Watch()
for event in w.stream(api.list_namespaced_custom_object, "example.com", "v1", "default", "widgets"):
    widget = event["object"]
    event_type = event["type"]

    name = widget["metadata"]["name"]
    color = widget["spec"]["color"]
    size = widget["spec"]["size"]

    print(f"🛠️ {event_type}: Widget '{name}' - Color: '{color}', Size: '{size}'")

    if event_type == "ADDED":
        print(f"✅ New Widget Created: {name} (Color: {color}, Size: {size})")
    elif event_type == "MODIFIED":
        print(f"🔄 Widget Updated: {name} (Color: {color}, Size: {size})")
    elif event_type == "DELETED":
        print(f"❌ Widget Deleted: {name}")
