using System;
using System.Drawing;
using Grasshopper.Kernel;

namespace pyumi
{
    public class pyumiInfo : GH_AssemblyInfo
    {
        public override string Name
        {
            get
            {
                return "pyumi";
            }
        }
        public override Bitmap Icon
        {
            get
            {
                //Return a 24x24 pixel bitmap to represent this GHA library.
                return null;
            }
        }
        public override string Description
        {
            get
            {
                //Return a short string describing the purpose of this GHA library.
                return "";
            }
        }
        public override Guid Id
        {
            get
            {
                return new Guid("6badf37d-227b-4952-b8e7-9f10e20a8298");
            }
        }

        public override string AuthorName
        {
            get
            {
                //Return a string identifying you or your company.
                return "CRON@SAP@MIT";
            }
        }
        public override string AuthorContact
        {
            get
            {
                //Return a string representing your preferred contact details.
                return "";
            }
        }
    }
}
