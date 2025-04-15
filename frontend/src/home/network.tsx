import { useNavigate } from "react-router-dom";
import { Button } from "@/components/ui/button";
import { useForm } from "react-hook-form";
import {
  Form,
  FormField,
  FormItem,
  FormLabel,
  FormControl,
  FormDescription,
  FormMessage,
} from "@/components/ui/form";

export default function Network() {
  const navigate = useNavigate();
  const form = useForm({
    defaultValues: {
      ipAddress: "",
      subnetMask: "",
    },
  });

  function onSubmit(values) {
    console.log(values);
    navigate("/simulation");
  }

  return (
    <div className="container mx-auto p-8">
      <h1 className="text-3xl font-bold mb-4">Network Configuration</h1>
      <Form {...form}>
        <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-4">
          <FormField
            name="ipAddress"
            control={form.control}
            rules={{ required: "IP Address is required" }}
            render={({ field }) => (
              <FormItem>
                <FormLabel>IP Address</FormLabel>
                <FormControl>
                  <input type="text" placeholder="Enter IP address" {...field} />
                </FormControl>
                <FormDescription>Please enter the IP address.</FormDescription>
                <FormMessage />
              </FormItem>
            )}
          />

          <FormField
            name="subnetMask"
            control={form.control}
            rules={{ required: "Subnet Mask is required" }}
            render={({ field }) => (
              <FormItem>
                <FormLabel>Subnet Mask</FormLabel>
                <FormControl>
                  <input type="text" placeholder="Enter subnet mask" {...field} />
                </FormControl>
                <FormDescription>Please enter the subnet mask.</FormDescription>
                <FormMessage />
              </FormItem>
            )}
          />

          <div className="flex gap-4">
            <Button variant="outline" onClick={() => navigate("/physical")}>
              Back
            </Button>
            <Button type="submit">Next: Simulation</Button>
          </div>
        </form>
      </Form>
    </div>
  );
}
