# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from chirpstack_api.as_pb.external.api import fuotaDeployment_pb2 as chirpstack__api_dot_as__pb_dot_external_dot_api_dot_fuotaDeployment__pb2


class FUOTADeploymentServiceStub(object):
    """FUOTADeploymentService is the service managing FUOTA deployments.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateForDevice = channel.unary_unary(
                '/api.FUOTADeploymentService/CreateForDevice',
                request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_fuotaDeployment__pb2.CreateFUOTADeploymentForDeviceRequest.SerializeToString,
                response_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_fuotaDeployment__pb2.CreateFUOTADeploymentForDeviceResponse.FromString,
                )
        self.Get = channel.unary_unary(
                '/api.FUOTADeploymentService/Get',
                request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_fuotaDeployment__pb2.GetFUOTADeploymentRequest.SerializeToString,
                response_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_fuotaDeployment__pb2.GetFUOTADeploymentResponse.FromString,
                )
        self.List = channel.unary_unary(
                '/api.FUOTADeploymentService/List',
                request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_fuotaDeployment__pb2.ListFUOTADeploymentRequest.SerializeToString,
                response_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_fuotaDeployment__pb2.ListFUOTADeploymentResponse.FromString,
                )
        self.GetDeploymentDevice = channel.unary_unary(
                '/api.FUOTADeploymentService/GetDeploymentDevice',
                request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_fuotaDeployment__pb2.GetFUOTADeploymentDeviceRequest.SerializeToString,
                response_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_fuotaDeployment__pb2.GetFUOTADeploymentDeviceResponse.FromString,
                )
        self.ListDeploymentDevices = channel.unary_unary(
                '/api.FUOTADeploymentService/ListDeploymentDevices',
                request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_fuotaDeployment__pb2.ListFUOTADeploymentDevicesRequest.SerializeToString,
                response_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_fuotaDeployment__pb2.ListFUOTADeploymentDevicesResponse.FromString,
                )


class FUOTADeploymentServiceServicer(object):
    """FUOTADeploymentService is the service managing FUOTA deployments.
    """

    def CreateForDevice(self, request, context):
        """CreateForDevice creates a deployment for the given DevEUI.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Get returns the fuota deployment for the given id.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """List lists the fuota deployments.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDeploymentDevice(self, request, context):
        """GetDeploymentDevice returns the deployment device.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListDeploymentDevices(self, request, context):
        """ListDeploymentDevices lists the devices (and status) for the given fuota deployment ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FUOTADeploymentServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateForDevice': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateForDevice,
                    request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_fuotaDeployment__pb2.CreateFUOTADeploymentForDeviceRequest.FromString,
                    response_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_fuotaDeployment__pb2.CreateFUOTADeploymentForDeviceResponse.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_fuotaDeployment__pb2.GetFUOTADeploymentRequest.FromString,
                    response_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_fuotaDeployment__pb2.GetFUOTADeploymentResponse.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_fuotaDeployment__pb2.ListFUOTADeploymentRequest.FromString,
                    response_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_fuotaDeployment__pb2.ListFUOTADeploymentResponse.SerializeToString,
            ),
            'GetDeploymentDevice': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDeploymentDevice,
                    request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_fuotaDeployment__pb2.GetFUOTADeploymentDeviceRequest.FromString,
                    response_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_fuotaDeployment__pb2.GetFUOTADeploymentDeviceResponse.SerializeToString,
            ),
            'ListDeploymentDevices': grpc.unary_unary_rpc_method_handler(
                    servicer.ListDeploymentDevices,
                    request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_fuotaDeployment__pb2.ListFUOTADeploymentDevicesRequest.FromString,
                    response_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_fuotaDeployment__pb2.ListFUOTADeploymentDevicesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'api.FUOTADeploymentService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FUOTADeploymentService(object):
    """FUOTADeploymentService is the service managing FUOTA deployments.
    """

    @staticmethod
    def CreateForDevice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.FUOTADeploymentService/CreateForDevice',
            chirpstack__api_dot_as__pb_dot_external_dot_api_dot_fuotaDeployment__pb2.CreateFUOTADeploymentForDeviceRequest.SerializeToString,
            chirpstack__api_dot_as__pb_dot_external_dot_api_dot_fuotaDeployment__pb2.CreateFUOTADeploymentForDeviceResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.FUOTADeploymentService/Get',
            chirpstack__api_dot_as__pb_dot_external_dot_api_dot_fuotaDeployment__pb2.GetFUOTADeploymentRequest.SerializeToString,
            chirpstack__api_dot_as__pb_dot_external_dot_api_dot_fuotaDeployment__pb2.GetFUOTADeploymentResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.FUOTADeploymentService/List',
            chirpstack__api_dot_as__pb_dot_external_dot_api_dot_fuotaDeployment__pb2.ListFUOTADeploymentRequest.SerializeToString,
            chirpstack__api_dot_as__pb_dot_external_dot_api_dot_fuotaDeployment__pb2.ListFUOTADeploymentResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDeploymentDevice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.FUOTADeploymentService/GetDeploymentDevice',
            chirpstack__api_dot_as__pb_dot_external_dot_api_dot_fuotaDeployment__pb2.GetFUOTADeploymentDeviceRequest.SerializeToString,
            chirpstack__api_dot_as__pb_dot_external_dot_api_dot_fuotaDeployment__pb2.GetFUOTADeploymentDeviceResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListDeploymentDevices(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.FUOTADeploymentService/ListDeploymentDevices',
            chirpstack__api_dot_as__pb_dot_external_dot_api_dot_fuotaDeployment__pb2.ListFUOTADeploymentDevicesRequest.SerializeToString,
            chirpstack__api_dot_as__pb_dot_external_dot_api_dot_fuotaDeployment__pb2.ListFUOTADeploymentDevicesResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
