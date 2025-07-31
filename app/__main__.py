import pulumi
from pulumi_kubernetes.core.v1 import Namespace, Service, Pod

# Configuration
config = pulumi.Config()
app_name = "nginx"
labels = {"app": app_name}

# Namespace
ns = Namespace("web-ns")

# Pod
pod = Pod(
    app_name,
    metadata={"namespace": ns.metadata["name"], "labels": labels},
    spec={
        "containers": [{
            "name": "nginx",
            "image": "nginx:latest",
            "ports": [{"containerPort": 80}]
        }]
    },
)

# Service (ClusterIP)
service = Service(
    f"{app_name}-svc",
    metadata={"namespace": ns.metadata["name"]},
    spec={
        "selector": labels,
        "ports": [{"port": 80, "targetPort": 80}],
        # "type": "ClusterIP"  # optional, since it's the default
    },
)

# Export service cluster IP
pulumi.export("cluster_ip", service.spec.apply(lambda s: s.cluster_ip))
